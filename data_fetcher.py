import requests

# API Constants
API_URL = "https://api.api-ninja.com/v1/animals"
API_KEY = "gR/VxO32JnWUv555uz2nQQ==VZUv1hfXQQUH5XMz"

def fetch_data(animal_name):
    """
    Fetches the data for the animal 'animal_name' from the API.
    Returns: A list of animals, each animal represented as a dictionary:
    {
        'name': ...,
        'taxonomy': {...},
        'locations': [...],
        'characteristics': {...}
    }
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
