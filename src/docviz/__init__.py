import asyncio
import threading

from .constants import get_docviz_directory
from .environment import check_dependencies
from .lib.document.class_ import Document
from .lib.functions import (
    batch_extract,
    extract_content,
    extract_content_streaming,
    extract_content_streaming_sync,
    extract_content_sync,
)
from .types import (
    DetectionConfig,
    ExtractionChunk,
    ExtractionConfig,
    ExtractionEntry,
    ExtractionResult,
    ExtractionType,
    LLMConfig,
    OCRConfig,
    SaveFormat,
)

__DEPENDENCIES_CHECKED = False
__DEPENDENCIES_LOCK = threading.Lock()


def _check_dependencies_once():
    """
    Ensure dependencies are checked only once in a thread-safe and process-safe manner.

    This function is called automatically on module import to verify that all required
    dependencies (models, libraries, etc.) are available before document processing.
    This prevents runtime errors and provides early feedback about missing dependencies.

    A global variable tracks whether dependencies have been checked in the current thread.
    For process-level safety, a lock file at ~/.docviz/dependencies_checked.lock prevents
    multiple processes from performing the check simultaneously. Double-checked locking
    is used to minimize unnecessary locking and improve performance.

    The function handles different asyncio contexts:
    - Creates a new event loop if none exists
    - Uses asyncio.run() for clean execution
    - Handles cases where event loop is already running (e.g., Jupyter notebooks)

    Raises:
        Exception: If any required dependency is missing or the dependency check fails.
            The specific exception type depends on what dependency is missing (e.g.,
            FileNotFoundError for missing models, ImportError for missing packages).
    """
    global __DEPENDENCIES_CHECKED

    # Use a lock file to ensure this runs only once across processes
    lock_file = get_docviz_directory() / "dependencies_checked.lock"
    lock_file.parent.mkdir(exist_ok=True)

    # Check if already verified in this session or globally
    if __DEPENDENCIES_CHECKED or lock_file.exists():
        return

    with __DEPENDENCIES_LOCK:
        # Double-check pattern
        if __DEPENDENCIES_CHECKED or lock_file.exists():
            return

        try:
            _run_async_dependency_check()

            __DEPENDENCIES_CHECKED = True
            lock_file.touch()

        except Exception as e:
            # If dependencies check fails, don't mark as checked
            # so it will retry next time
            raise e


def _run_async_dependency_check():
    """
    Run the async dependency check with proper event loop handling.

    This helper function handles different asyncio contexts gracefully:
    1. If no event loop is running, use asyncio.run() (preferred modern approach)
    2. If an event loop is already running (e.g., in Jupyter), create a new thread
    3. Handle various edge cases and provide clear error messages

    Raises:
        RuntimeError: If dependency check fails after multiple attempts
        Exception: Original exception from check_dependencies() if it's not event loop related
    """
    try:
        asyncio.run(check_dependencies())
    except RuntimeError as e:
        error_msg = str(e).lower()

        # Handle "asyncio.run() cannot be called from a running event loop"
        if "cannot be called from a running event loop" in error_msg:
            # We're in an environment with a running event loop (e.g., Jupyter)
            # Run in a separate thread to avoid conflicts
            import concurrent.futures

            def run_in_thread():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    return loop.run_until_complete(check_dependencies())
                finally:
                    loop.close()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(run_in_thread)
                future.result()
        else:
            # Re-raise other RuntimeErrors
            raise


# Check dependencies on import
_check_dependencies_once()

__all__ = [
    "DetectionConfig",
    "Document",
    "ExtractionChunk",
    "ExtractionConfig",
    "ExtractionEntry",
    "ExtractionResult",
    "ExtractionType",
    "LLMConfig",
    "OCRConfig",
    "SaveFormat",
    "batch_extract",
    "extract_content",
    "extract_content_streaming",
    "extract_content_streaming_sync",
    "extract_content_sync",
]
