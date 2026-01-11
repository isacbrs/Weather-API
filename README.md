#  🌤️ Weather API

A RESTful API built with **FastAPI** that returns current weather information for a given city, using a third-party weather service provider.

This project is a solution for the **roadmap.sh Weather API project**:  
https://roadmap.sh/projects/weather-api-wrapper-service

---

##  Features

- Get current weather data by city name
- Fetches real-time data from an external weather API
- Proper error handling for invalid cities or unavailable services
- API key managed securely using environment variables

---

## Tech Stack

- Python
- FastAPI
- Requests
- Uvicorn

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/isacbrs/weather-api.git
cd weather-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment variables

Create a `.env` file at the project root:

```env
WEATHER_API_KEY=your_api_key_here
```

> The `.env` file is ignored by Git for security reasons.

---

## Running the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000/weather
```

---

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## 📌 Example Request

```
http://127.0.0.1:8000/weather?city=Brasilia
```

### Example Response

```json
{
  "city": "Brasília",
  "temperature": 27.3,
  "humidity": 65,
  "description": "Partly cloudy"
}
```

---

##  Architecture Notes

In a production scenario, this API could benefit from an in-memory cache (e.g., **Redis**) to reduce repeated calls to the external weather provider and improve performance.

In this first version, the API always fetches fresh data directly from the external service to keep the architecture simple and focused on core API concepts.
