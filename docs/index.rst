Welcome to docviz-python documentation!
=======================================

.. image:: https://raw.githubusercontent.com/privateai-com/docviz/refs/heads/main/assets/header_long.svg
   :alt: docviz
   :width: 100%

**Extract content from documents easily with Python.**

`docviz-python <https://github.com/privateai-com/docviz>`_ is a robust Python library for extracting and analyzing content from documents. It offers batch and selective extraction, flexible configuration options, and supports multiple output formats.

GitHub: https://github.com/privateai-com/docviz

Try docviz Online on our website
--------------------------------

You can test docviz functionality directly in your browser without any installation.

.. raw:: html

   <div style="text-align: left; margin: 30px 0;">
       <a href="https://demo.privateai.com" 
          style="display: inline-block; 
                 background: #667eea; 
                 text-align: center;
                 color: white; 
                 padding: 15px 30px; 
                 text-decoration: none; 
                 border-radius: 8px; 
                 font-size: 18px; 
                 font-weight: bold; 
                 box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
                 transition: all 0.3s ease;
                 border: none;
                 cursor: pointer;
                 width: 70%;">
           🚀 Try docviz Demo
       </a>
   </div>

   <style>
       a:hover {
           transform: translateY(-2px);
           box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
       }
   </style>

Getting Started with the Web Interface
--------------------------------------

Follow these simple steps to process your documents online:

1. **Create an Account**
   
   .. image:: /_static/login-page.png
      :alt: Login page screenshot
      :width: 80%
      :align: center
   
   Visit the website and register for a new account to access the docviz interface.

2. **Navigate to docviz**
   
   .. image:: /_static/main-page.png
      :alt: Main dashboard screenshot
      :width: 80%
      :align: center
   
   Once logged in, locate and click on the "docviz" tab in the left sidebar to access the document processing interface.

3. **Upload Your PDF**
   
   .. image:: /_static/upload-page.png
      :alt: docviz upload interface screenshot
      :width: 80%
      :align: center
   
   Upload your PDF file using the "Upload PDF" field. The system will automatically begin processing your document.
   
   .. note::
      **File Size Limit**: The maximum file size is 50 MB. Larger files will be rejected during upload.
      
      **File Retention**: Uploaded files are stored on our servers for exactly 7 days, after which they are automatically deleted for security and privacy reasons.

4. **Wait for Processing**
   
   The system will process your document in the background. You can monitor the progress as the file is analyzed and content is extracted.

5. **Download Results**
   
   Once processing is complete, you'll see a green "success" indicator next to your document along with a "Download" button to retrieve the results.

6. **View and Explore Results**
   
   .. image:: /_static/result-page.png
      :alt: Document results overview screenshot
      :width: 80%
      :align: center
   
   Click on the document card to view detailed results organized by content type:
   
   - **Text**: Extracted textual content
   - **Tables**: Structured tabular data
   - **Images**: Detected visual elements
   - **Formulas**: Mathematical equations and expressions
   
   Results are available in JSON format for easy integration with your applications.

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
