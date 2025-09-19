"""
Example demonstrating how to use custom prompts for chart summarization.

This example shows how to configure a custom prompt for the chart summarizer
to get more specific or tailored output from the LLM.
"""

import os
import docviz


def main():
    """Demonstrate custom prompt usage for chart summarization."""
    
    # Example 1: Business-focused prompt
    business_prompt = """
    Analyze this chart from a business perspective and provide:
    1. Key performance indicators and metrics
    2. Trends and patterns that indicate business performance
    3. Potential opportunities or concerns
    4. Actionable insights for decision makers
    """
    
    business_config = docviz.LLMConfig(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"),
        base_url="https://api.openai.com/v1",
        custom_prompt=business_prompt
    )
    
    # Example 2: Technical analysis prompt
    technical_prompt = """
    Provide a technical analysis of this chart including:
    1. Data structure and format
    2. Statistical properties and distributions
    3. Mathematical relationships
    4. Technical specifications and parameters
    """
    
    technical_config = docviz.LLMConfig(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"),
        base_url="https://api.openai.com/v1",
        custom_prompt=technical_prompt
    )
    
    # Example 3: Simple summary prompt
    simple_prompt = "Summarize the key information from this chart in 2-3 sentences."
    
    simple_config = docviz.LLMConfig(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"),
        base_url="https://api.openai.com/v1",
        custom_prompt=simple_prompt
    )
    
    # Example usage with a document
    document_path = "examples/data/2_pages_doc.pdf"
    
    if os.path.exists(document_path):
        print("Processing document with business-focused prompt...")
        document = docviz.Document(document_path)
        
        # Extract content with custom prompt
        extractions = document.extract_content_sync(
            llm_config=business_config,
            includes=[docviz.ExtractionType.CHARTS]
        )
        
        print("Extraction completed with custom prompt!")
        print(f"Found {len(extractions)} pages with content")
        
        # Save results
        extractions.save("examples/results/custom_prompt_output", save_format=docviz.SaveFormat.JSON)
        print("Results saved to examples/results/custom_prompt_output.json")
    else:
        print(f"Document not found: {document_path}")
        print("Please ensure the example document exists before running this example.")


if __name__ == "__main__":
    main()
