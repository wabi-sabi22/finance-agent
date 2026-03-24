# app/services/tools.py
from typing import List, Dict, Any

class WebSearchService:
    def __init__(self):
        self._client = None
    
    def search_finance(self, query: str, max_results: int = 3) -> List[dict]:
        """Perform a financial search and return both content and source URL."""
        if self._client is None:
            return []

        try:
            resp = self._client.search(
                query=query,
                max_results=max_results,
                search_depth="basic",
                topic="finance",
                include_answer=False,
            )
        except Exception:
            return []

        results: List[dict] = []
        for item in resp.get("results", []):
            # We capture both the text and the link now
            results.append({
                "content": item.get("content", ""),
                "url": item.get("url", "No link available")
            })
        return results 
web_search_service = WebSearchService() 