# Contributing to docviz-python

Thank you for your interest in contributing to docviz-python! This document provides guidelines and information for contributors.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a virtual environment** using uv
4. **Install dependencies** in development mode

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/docviz.git
cd docviz

# Create virtual environment and install
uv sync
uv pip install -e ".[dev]"
```

## Code Style

docviz-python follows strict coding standards:

* **Type hints**: All functions must have type hints
* **Docstrings**: Use Google-style docstrings
* **Formatting**: Use ruff for formatting and linting
* **Naming**: Refer to the Python PEP 8 style guide
* **TYPE_CHECKING**: Refer to the Python PEP 484 type hints

Example of proper code style:

```python
def extract_content(
    document_path: str,
    config: ExtractionConfig | None = None,
) -> ExtractionResult:
    """
    Extract content from a document.

    Args:
        document_path: Path to the document file
        config: Optional extraction configuration

    Returns:
        ExtractionResult containing extracted content

    Raises:
        FileNotFoundError: If document file doesn't exist
        ValueError: If document format is not supported
    """
    if not Path(document_path).exists():
        raise FileNotFoundError(f"Document not found: {document_path}")
    
    # Implementation here
    return result
```

## Code Quality Checks

Run quality checks:

```bash
uv run tools/quality_check.py <path_to_target>
```

for example:

```bash
uv run tools/quality_check.py src/
```

## Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards

3. **Update documentation** if needed

4. **Run quality checks**:
   ```bash
   uv run python tools/quality_check.py src/
   ```

5. **Commit your changes** with a descriptive message:
   ```bash
   git commit -m "feat: add new extraction feature"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a pull request** on GitHub

## Commit Message Format

Use conventional commit messages:

* `feat:` - New features
* `fix:` - Bug fixes
* `docs:` - Documentation changes
* `style:` - Code style changes
* `refactor:` - Code refactoring
* `test:` - Test additions or changes
* `chore:` - Maintenance tasks

Examples:
```bash
feat: add support for Excel output format
fix: resolve memory leak in batch processing
docs: update installation instructions
test: add tests for URL document loading
```

## Issue Reporting

When reporting issues, please include:

1. **Environment**: Python version, OS, docviz version
2. **Reproduction**: Steps to reproduce the issue
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Error messages**: Full error traceback
6. **Sample files**: If applicable, provide sample documents

Example issue:

```markdown
## Environment

- Python: 3.11.0
- OS: Ubuntu 22.04
- docviz-python: 0.10.1

## Issue

When extracting tables from PDFs with complex layouts, some table cells are missing.

## Steps to Reproduce

1. Load a PDF with complex table layout
2. Extract content with `includes=[ExtractionType.TABLE]`
3. Check the extracted table data

## Expected Behavior

All table cells should be extracted correctly.

## Actual Behavior

Some cells in the middle of tables are empty or missing.

## Error Messages

No errors, but incomplete data extraction.
```

## Documentation

When contributing documentation:

1. **Use RST format** for Sphinx documentation
2. **Include code examples** that work
3. **Update API docs** for new features
4. **Add type hints** in docstrings
5. **Test documentation** builds correctly

### Building Documentation

```bash
# Install documentation dependencies
uv pip install sphinx sphinx-rtd-theme sphinx-copybutton

# Build documentation
sphinx-build -b html docs/ _build/html/

# View documentation
open _build/html/index.html
```

## Getting Help

* **GitHub Issues**: For bug reports and feature requests
* **Documentation**: Check the docs for usage examples

Thank you for contributing to docviz-python!
