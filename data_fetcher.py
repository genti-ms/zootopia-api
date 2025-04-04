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

# main
animal_name = input("Please enter an animal name: ") 
data = fetch_data(animal_name)

# Print the fetched data
if data:
    print(f"Data for {animal_name}:")
    for animal in data:
        print(animal)
else:
    print(f"No data found for {animal_name}.")
