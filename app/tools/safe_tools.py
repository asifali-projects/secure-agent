from datetime import datetime, timezone


async def get_time():

    return {
        "utc": datetime.now(
            timezone.utc
        ).isoformat()
    }


async def search_documents(
    query: str,
):

    # Real Qdrant implementation will be connected
    # in the RAG layer.
    return {
        "query": query,
        "results": [],
    }