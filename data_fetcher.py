import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variable
API_KEY = os.getenv('API_KEY')

# API URL
API_URL = "https://api.example.com/data"

def fetch_data(animal_name):
    """
    Fetches data for the given animal from the API.
    Returns: List of animals (dictionaries).
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

#main
animal_name = "fox"
data = fetch_data(animal_name)
print(data)
