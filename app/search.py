from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os
from pathlib import Path
from dotenv import load_dotenv

# Force-load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

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
