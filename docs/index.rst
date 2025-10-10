Welcome to docviz-python documentation!
=======================================

.. image:: https://raw.githubusercontent.com/privateai-com/docviz/refs/heads/main/assets/header_long.svg
   :alt: docviz
   :width: 100%

**Extract content from documents easily with Python.**

`docviz-python <https://github.com/privateai-com/docviz>`_ is a robust Python library for extracting and analyzing content from documents. It offers batch and selective extraction, flexible configuration options, and supports multiple output formats.

GitHub: https://github.com/privateai-com/docviz

Key Features
------------

- **PDF Support**: Extract content from PDF documents (other formats coming soon)
- **URL Inputs**: Load documents from local paths or HTTP(S) URLs
- **Streaming Extraction**: Process large documents with real-time results
- **Batch Processing**: Handle multiple files efficiently
- **Chunked Extraction**: Process documents in configurable page chunks
- **Selective Extraction**: Choose what to extract (tables, text, figures, equations, etc.)
- **Multiple Output Formats**: Export to JSON, CSV, Excel, XML
- **CLI Included**: `docviz` command for single-file and batch processing
- **Async Support**: Both synchronous and asynchronous processing
- **Chart Detection & LLM Summarization (optional)**: Detect visual elements and optionally summarize charts using an LLM
- **Automatic Dependencies**: On first import, downloads required models and helps install Tesseract on Windows

Quick Start
----------

.. code-block:: python

    import asyncio
    import docviz

    async def main():
        # Create a document instance
        document = docviz.Document("path/to/your/document.pdf")
        
        # Extract all content asynchronously
        extractions = await document.extract_content()
        
        # Save results
        extractions.save("results", save_format=docviz.SaveFormat.JSON)

    asyncio.run(main())

Installation
-----------

Using uv (recommended):

.. code-block:: bash

    uv add docviz-python

Using pip:

.. code-block:: bash

    pip install docviz-python

Package Structure
----------------

For a detailed overview of the package structure and components, see :doc:`package_structure`.

Table of Contents
==================

.. toctree::
   :maxdepth: 4
   
   quickstart
   user_guide/index
   api/index
   examples/index
   package_structure
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
