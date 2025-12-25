from fastapi import APIRouter, Depends, HTTPException
from app.services.search_service import fetch_market_data
from app.services.ai_service import analyze_with_ai
from app.security.auth import verify_api_key
from app.security.rate_limit import rate_limit

router = APIRouter()

@router.get("/analyze/{sector}", summary="Analyze Sector")
@rate_limit
def analyze_sector(
    sector: str,
    _ = Depends(verify_api_key)
):
    data = fetch_market_data(sector)
    if not data:
        raise HTTPException(status_code=502, detail="Market data fetch failed")

    report = analyze_with_ai(sector, data)
    return {
        "sector": sector,
        "report_markdown": report
    }
