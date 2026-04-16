import requests
from etl.logger import logger

API_URL = "https://services2.arcgis.com/5I7u4SJE1vUr79JC/arcgis/rest/services/UniversityChapters_Public/FeatureServer/0/query"

def fetch_chapters():
    params = {
        "where": "1=1",
        "outFields": "*",
        "outSR": "4326",
        "f": "json"
    }
    try:
         response = requests.get(API_URL, params=params)
         response.raise_for_status()
         return response.json()

    except requests.exceptions.RequestException as e:
         logger.error(f"API request failed: {e}")
         raise