# backend/app/azure_search.py

import requests # type: ignore
from .config import AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_API_KEY, AZURE_SEARCH_INDEX_NAME

def search_azure(query: str):
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_SEARCH_API_KEY,
    }

    payload = {
        "search": query,
        "top": 1,  # 获取最相关的一个结果
    }

    url = f"{AZURE_SEARCH_ENDPOINT}/indexes/{AZURE_SEARCH_INDEX_NAME}/docs/search?api-version=2021-04-30-Preview"
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        search_results = response.json()
        if "value" in search_results and len(search_results["value"]) > 0:
            return search_results["value"][0]["content"]  # 假设结果中有 content 字段
        else:
            return "No relevant results found."
    else:
        return "Error with Azure Search API."

