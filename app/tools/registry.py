from app.tools.safe_tools import (
    get_time,
    search_documents,
)


TOOLS = {
    "get_time": get_time,
    "search_documents": search_documents,
}


def get_tool(name: str):

    return TOOLS.get(name)


def list_tools():

    return [
        {
            "name": name,
            "enabled": True,
        }
        for name in TOOLS
    ]