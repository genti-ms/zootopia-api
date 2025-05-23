import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches data for the given animal from the API.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list: A list of dictionaries containing animal information,
              or an empty list if the request fails.
    """
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API_KEY is not set. Please define it in the .env file.")

    response = requests.get(
        API_URL,
        params={"name": animal_name},
        headers={"X-Api-Key": api_key}
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
