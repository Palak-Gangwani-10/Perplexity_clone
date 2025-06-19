from config import Settings
from tavily import TavilyClient

settings = Settings()

class SearchService:
    def __init__(self):
        try:
            # Try to initialize Tavily client
            if settings.TAVILY_API_KEY and settings.TAVILY_API_KEY != "":
                self.tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)
                self.use_real_search = True
                print("✅ Tavily client initialized successfully")
            else:
                self.use_real_search = False
                print("⚠️ No Tavily API key found, using mock search")
        except Exception as e:
            self.use_real_search = False
            print(f"⚠️ Tavily initialization failed: {e}")

    def web_search(self, query: str):
        if self.use_real_search:
            try:
                # Real web search using Tavily
                print(f"🔍 Searching the web for: {query}")
                response = self.tavily_client.search(query, max_results=5)
                print(f"✅ Found {len(response.get('results', []))} results")
                return response
            except Exception as e:
                print(f"⚠️ Tavily API error: {e}")
        
        # Fallback to mock search
        print(f"🔍 Using mock search for: {query}")
        mock_response = {
            "results": [
                {"title": "Mock Result 1", "content": f"Mock search result for: {query}"},
                {"title": "Mock Result 2", "content": f"Additional information about: {query}"}
            ]
        }
        return mock_response