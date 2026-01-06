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

    data = response.json()

    return {
        "city": data["resolvedAddress"],
        "temperature": data["currentConditions"]["temp"],
        "humidity": data["currentConditions"]["humidity"],
        "description": data["currentConditions"]["conditions"]
    }
