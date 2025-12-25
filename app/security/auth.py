from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

API_KEY = "my-secret-key"

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    if not api_key:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    if api_key != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Invalid API key")
