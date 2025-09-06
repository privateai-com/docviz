import asyncio
import logging
import os

import docviz

logging.basicConfig(level=logging.INFO)


async def openai_api_example():
    document = docviz.Document(r"examples/data/2507.21509v1.pdf")

    extractions = await document.extract_content(
        extraction_config=docviz.ExtractionConfig(page_limit=3),
        llm_config=docviz.LLMConfig(
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY"),  # type: ignore
            base_url="https://api.openai.com/v1",
        ),
    )
    extractions.save(document.name, save_format=docviz.SaveFormat.JSON)


if __name__ == "__main__":
    asyncio.run(openai_api_example())
