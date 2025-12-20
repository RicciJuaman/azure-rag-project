from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
)

def retrieve_top_k(query: str, k: int = 10):
    results = search_client.search(
        search_text=query,
        top=k
    )

    docs = []
    for i, r in enumerate(results):
        docs.append({
            "id": i + 1,
            "content": r.get("content", ""),
            "source": r.get("source", "unknown")
        })

    return docs
