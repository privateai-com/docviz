import asyncio
import logging

import docviz

logging.basicConfig(level=logging.INFO)


async def streaming_example():
    document = docviz.Document(r"examples/data/2507.21509v1.pdf")

    async for page_result in document.extract_streaming(
        extraction_config=docviz.ExtractionConfig(page_limit=10),
        includes=docviz.types.IncludesPreset.TEXT_DATA,
    ):
        page_result.save(
            document.name + f"_page{page_result.page_number}",
            save_format=docviz.SaveFormat.JSON,
        )


if __name__ == "__main__":
    asyncio.run(streaming_example())
