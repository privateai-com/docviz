from pathlib import Path

import cv2
import numpy as np

from docviz.types import DetectionResult


def filter_detections(
    detections: list[DetectionResult],
    include: list[str] | None = None,
    exclude: list[str] | None = None,
    return_bboxes: bool = False,
) -> list[DetectionResult] | list[list[float]]:
    """
    Filter detections to only include elements with specified labels.

    Args:
        detections (List[DetectionResult]): List of all detections.
        labels (List[str]): List of lowercased labels to filter by.

    Returns:
        List[DetectionResult]: Filtered list containing only detections with specified labels.
    """
    if exclude is None:
        exclude = []
    if include is None:
        include = []

    result = []
    if include:
        result = [det for det in detections if det.label_name.lower() in include]
    elif exclude:
        result = [det for det in detections if det.label_name.lower() not in exclude]
    else:
        result = detections

    if return_bboxes:
        result = [det.bbox for det in result]

    return result


def load_rgb_image(image_path: Path) -> np.ndarray:
    """
    Load an image from the given path and convert it to RGB format.

    Args:
        image_path (Path): Path to the image file.

    Returns:
        np.ndarray: Image in RGB format.
    """
    image_bgr: np.ndarray | None = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if image_bgr is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    image_rgb: np.ndarray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return image_rgb
