# data_fetcher.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches data for the given animal from the API.
    Returns a list of animals (dictionaries).
    """
    response = requests.get(
        API_URL,
        params={"name": animal_name},
        headers={"X-Api-Key": API_KEY}
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
