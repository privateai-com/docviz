from enum import Enum

from docviz.types.extraction_type import ExtractionType


class IncludesPreset(list, Enum):
    """Preset for includes."""

    TEXT_DATA = [
        ExtractionType.TEXT,
        ExtractionType.EQUATION,
        ExtractionType.OTHER,
    ]
    MEDIA = [
        ExtractionType.FIGURE,
        ExtractionType.TABLE,
    ]
