import json


# Function to load the JSON file
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load the data from the JSON file
animals_data = load_data('animals_data.json')

# Iterate through the animals data and print the required information
for animal in animals_data:
    # Print Name if available
    if 'name' in animal:
        print(f"Name: {animal['name']}")

    # Print Diet if available (from the 'characteristics' dictionary)
    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        print(f"Diet: {animal['characteristics']['diet']}")

    # Print Location if available
    if 'locations' in animal and animal['locations']:
        print(f"Location: {animal['locations'][0]}")

    # Print Type if available (from the 'characteristics' dictionary)
    if 'characteristics' in animal and 'type' in animal['characteristics']:
        print(f"Type: {animal['characteristics']['type']}")

    print()
