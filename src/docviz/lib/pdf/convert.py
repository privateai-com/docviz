import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from functools import lru_cache
from pathlib import Path

import fitz

from docviz.logging import get_logger

logger = get_logger(__name__)


@lru_cache(maxsize=1)
def get_optimal_worker_count() -> int:
    """Get optimal number of workers based on CPU count.

    Returns:
        Optimal number of workers (CPU count, with minimum of 1 and maximum of 16).
    """
    try:
        cpu_count = os.cpu_count() or 1 if os.name == "nt" else len(os.sched_getaffinity(0)) or 1
    except Exception as e:
        logger.warning(f"Could not determine optimal worker count: {e}")
        cpu_count = 1
    return min(max(cpu_count, 1), 16)


def _render_page_to_png(
    pdf_path: str,
    output_dir: str,
    page_num: int,
    zoom_x: float,
    zoom_y: float,
    colorspace: str,
) -> str:
    """
    Render a single page of a PDF to a PNG file.

    Args:
        pdf_path (str): Path to the PDF file.
        output_dir (str): Directory to save PNG images.
        page_num (int): Page number to render (0-based).
        zoom_x (float): Horizontal zoom factor.
        zoom_y (float): Vertical zoom factor.
        colorspace (str): Colorspace for output image.

    Returns:
        str: Path to the saved PNG file.
    """
    logger.debug(f"Rendering page {page_num + 1} from {pdf_path}")

    with fitz.open(pdf_path) as doc:
        matrix = fitz.Matrix(zoom_x, zoom_y)
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=matrix, colorspace=colorspace, alpha=False)  # type: ignore[attr-defined]
        img_path = str(Path(output_dir) / f"page_{page_num + 1}.png")
        pix.save(img_path)
        logger.debug(f"Saved page {page_num + 1} to {img_path}")
    return img_path


def pdf_to_pngs(
    pdf_path: str,
    output_dir: str,
    zoom_x: float = 5,
    zoom_y: float = 5,
    colorspace: str = "rgb",
    max_workers: int | None = None,
) -> list[Path]:
    """
    Convert each page of a PDF to a very high-quality PNG file using PyMuPDF and process pool.

    Args:
        pdf_path (str): Path to the PDF file.
        output_dir (str): Directory to save PNG images.
        zoom_x (float): Horizontal zoom factor for rendering quality.
        zoom_y (float): Vertical zoom factor for rendering quality.
        colorspace (str): Colorspace for output image ("rgb" or "gray").
        max_workers (int, optional): Maximum number of worker processes.
            If None, uses optimal count based on CPU cores.

    Returns:
        List[Path]: List of PNG file paths as Path objects.
    """
    logger.info(f"Converting PDF to PNG: {pdf_path}")
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"Zoom factors: x={zoom_x}, y={zoom_y}")
    logger.info(f"Colorspace: {colorspace}")

    # Determine optimal number of workers
    if max_workers is None:
        max_workers = get_optimal_worker_count()
    else:
        max_workers = min(max(max_workers, 1), 16)  # Ensure reasonable bounds

    logger.info(f"Using {max_workers} worker processes for PDF conversion")

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    with fitz.open(pdf_path) as doc:
        num_pages = len(doc)
    logger.info(f"PDF has {num_pages} pages")

    # For small documents, use fewer workers to avoid overhead
    actual_workers = min(max_workers, num_pages)
    if actual_workers < max_workers:
        logger.debug(f"Reducing workers to {actual_workers} for {num_pages} pages")

    image_paths: list[Path] = []
    with ProcessPoolExecutor(max_workers=actual_workers) as executor:
        logger.debug(f"Starting parallel PDF rendering with {actual_workers} workers")
        futures = [
            executor.submit(
                _render_page_to_png,
                pdf_path,
                output_dir,
                page_num,
                zoom_x,
                zoom_y,
                colorspace,
            )
            for page_num in range(num_pages)
        ]
        for future in as_completed(futures):
            img_path = future.result()
            image_paths.append(Path(img_path))

    image_paths.sort(key=lambda p: int(p.stem.split("_")[1]))
    logger.info(f"Successfully converted {len(image_paths)} pages to PNG")
    return image_paths


def extract_pages(
    pdf_path: Path,
    output_dir: Path,
    pages_to_extract: list[int],
    zoom_x: float = 5,
    zoom_y: float = 5,
    colorspace: str = "rgb",
    max_workers: int | None = None,
) -> list[Path]:
    """
    Extract specific pages from a PDF and save them as PNG files using a process pool.

    Args:
        pdf_path: Path to the PDF file.
        output_dir: Directory to save PNG images.
        pages_to_extract: List of page numbers to extract.
        zoom_x: Horizontal zoom factor for rendering quality.
        zoom_y: Vertical zoom factor for rendering quality.
        colorspace: Colorspace for output image ("rgb" or "gray").
        max_workers: Maximum number of worker processes. If None, uses optimal count.

    Returns:
        List of Paths to the saved PNG files.
    """
    # Determine optimal number of workers
    if max_workers is None:
        max_workers = get_optimal_worker_count()
    else:
        max_workers = min(max(max_workers, 1), 16)  # Ensure reasonable bounds

    # For small page sets, use fewer workers to avoid overhead
    actual_workers = min(max_workers, len(pages_to_extract))

    logger.info(f"Extracting {len(pages_to_extract)} pages using {actual_workers} workers")

    output_dir.mkdir(parents=True, exist_ok=True)
    image_paths: list[Path] = []
    with ProcessPoolExecutor(max_workers=actual_workers) as executor:
        futures = [
            executor.submit(
                _render_page_to_png,
                str(pdf_path),
                str(output_dir),
                page_num - 1,
                zoom_x,
                zoom_y,
                colorspace,
            )
            for page_num in pages_to_extract
        ]
        for future in as_completed(futures):
            image_paths.append(Path(future.result()))
    image_paths.sort(key=lambda p: int(p.stem.split("_")[1]))
    return image_paths
