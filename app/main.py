from fastapi import FastAPI
from fastapi.security import APIKeyHeader
from app.api.analyze import router

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

app = FastAPI(
    title="Trade Opportunities API",
    version="0.1.0"
)

app.include_router(router)
