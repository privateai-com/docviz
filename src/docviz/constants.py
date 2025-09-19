from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def get_docviz_directory() -> Path:
    """Get the docviz configuration directory.

    Returns:
        Path to the docviz directory.
    """
    return Path.home() / ".docviz"


# Performance and Processing Constants
DEFAULT_CHUNK_SIZE = 8192
DOWNLOAD_TIMEOUT_SECONDS = 30

# Default Detection Configuration Constants
DEFAULT_IMAGE_SIZE = 1024
DEFAULT_CONFIDENCE_THRESHOLD = 0.5
DEFAULT_DEVICE = "cpu"
DEFAULT_MODEL_FILE = "doclayout_yolo_docstructbench_imgsz1024.pt"

# Default Extraction Configuration Constants
DEFAULT_ZOOM_X = 3.0
DEFAULT_ZOOM_Y = 3.0
DEFAULT_PDF_TEXT_THRESHOLD_CHARS = 1000
DEFAULT_PREFER_PDF_TEXT = False

# Default OCR Configuration Constants
DEFAULT_OCR_LANGUAGE = "eng"
DEFAULT_LABELS_TO_EXCLUDE_OCR = [
    # CanonicalLabel.OTHER.value,
    # CanonicalLabel.PAGE_FOOTER.value,
    # CanonicalLabel.PAGE_HEADER.value,
    # CanonicalLabel.FOOTNOTE.value,
    "other",
    "page_footer",
    "page_header",
    "footnote",
    "picture",
    "table",
    "formula",
    "equation",
]

# Default LLM Configuration Constants
DEFAULT_LLM_MODEL = "gemma3"
DEFAULT_LLM_API_KEY = "dummy-key"
DEFAULT_LLM_BASE_URL = "http://localhost:11434/v1"

# Default Chunked Extraction Constants
DEFAULT_EXTRACTION_CHUNK_SIZE = 10

DEFAULT_VISION_PROMPT = """
You are a data extraction specialist. Your task is to extract ALL concrete, factual data from the image and present it in a structured, machine-readable format. Focus on extracting actual data, not interpretations or summaries.

CRITICAL INSTRUCTIONS:
- Extract EXACT values, numbers, labels, and text as they appear
- Do NOT paraphrase or interpret - present raw data
- Do NOT add analysis or conclusions unless specifically requested
- Extract ALL visible text, numbers, and data points
- Preserve the original structure and relationships

REQUIRED OUTPUT FORMAT:

**VISUAL TYPE**: [Chart/Table/Diagram/Flowchart/Graph/Other - be specific]

**EXTRACTED DATA**:
- All visible text (titles, labels, captions, annotations)
- All numerical values (exact numbers, percentages, coordinates)
- All categorical data (categories, groups, classifications)
- All relationships (connections, flows, hierarchies)

**STRUCTURED DATA**:
- Tables: Present as rows and columns with exact values
- Charts: List all data points with their exact values
- Diagrams: Extract all text labels and connections
- Flowcharts: List all steps, decisions, and connections

**TEXT CONTENT**:
- Extract ALL visible text exactly as written
- Include any captions, footnotes, or annotations
- Preserve formatting where possible

**NUMERICAL DATA**:
- List all numbers, percentages, ratios, measurements
- Include units of measurement
- Note any scales or ranges

If the image contains no extractable data, state "No structured data found" and describe what you see.

Remember: Your goal is to create a complete textual representation of the image's data content, not to analyze or interpret it.
"""

# Tesseract Configuration Constants
TESSERACT_DEFAULT_WIN_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSERACT_WIN_SETUP_URL = "https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe"
TESSERACT_WIN_SETUP_FILENAME = "tesseract-ocr-w64-setup-5.5.0.20241111.exe"
TESSERACT_ADDITIONAL_WIN_PATHS = [
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    r"C:\Tesseract-OCR\tesseract.exe",
]

# Model Configuration Constants
BASE_MODELS_URL = "https://github.com/privateai-com/docviz/raw/main/models"
REQUIRED_MODELS = [
    "doclayout_yolo_docstructbench_imgsz1024.pt",
    "yolov12l-doclaynet.pt",
    "yolov12m-doclaynet.pt",
]


@lru_cache(maxsize=1)
def get_models_path() -> Path:
    """Get the models directory path.

    Returns:
        Path to the models directory.
    """
    return get_docviz_directory() / "models"


# Legacy constant for backward compatibility
MODELS_PATH = get_models_path()

TMP_DIR_PREFIX = "docviz"
DEFAULT_CHART_SUMMARIZER_RETRIES = 3
DEFAULT_CHART_SUMMARIZER_TIMEOUT = 5
DEFAULT_MEMORY_CLEANUP_INTERVAL = 10
