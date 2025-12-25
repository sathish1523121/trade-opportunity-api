import requests

def fetch_market_data(sector: str):
    try:
        query = f"India {sector} market news"
        url = f"https://duckduckgo.com/?q={query}"
        response = requests.get(url, timeout=5)
        return response.text[:3000]
    except Exception as e:
        return None

