import asyncio
import logging

import docviz

logging.basicConfig(level=logging.INFO)


async def simple_example():
    try:
        document = docviz.Document("https://arxiv.org/pdf/2401.00123.pdf")

        extractions = await document.extract_content(
            extraction_config=docviz.ExtractionConfig(page_limit=3),
            includes=[docviz.ExtractionType.TEXT],
        )
        extractions.save(document.name, save_format=docviz.SaveFormat.XML)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(simple_example())
