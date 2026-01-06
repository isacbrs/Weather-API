from fastapi import FastAPI, Query, HTTPException
import requests
from app.config import WEATHER_API_KEY
from urllib.parse import quote

app = FastAPI(title="Weather API")

@app.get("/weather")
def get_weather(city: str = Query(..., example="São Paulo")):
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="API key not configured")

    city_encoded = quote(city)

    url = (
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        f"{city_encoded}?unitGroup=metric&key={WEATHER_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail=response.text)
    
    if response.status_code == 500:
        raise HTTPException(
        status_code=503,
        detail="Weather service unavailable"
    )

    data = response.json()

    return {
        "city": str(data["resolvedAddress"]),
        "temperature": float(data["currentConditions"]["temp"]),
        "humidity": float(data["currentConditions"]["humidity"]),
        "description": str(data["currentConditions"]["conditions"])
    }   