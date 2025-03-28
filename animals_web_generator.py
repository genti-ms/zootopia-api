import json


def load_data(file_path):
    """Lädt eine JSON-Datei"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_data(animals):
    """Druckt die relevanten Daten für jedes Tier"""
    for animal in animals:
        if "name" in animal:
            print(f"Name: {animal['name']}")

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "diet" in characteristics:
                print(f"Diet: {characteristics['diet']}")

            if "locations" in animal and animal["locations"]:
                print(f"Location: {animal['locations'][0]}")

            if "type" in characteristics:
                print(f"Type: {characteristics['type']}")

        print()


if __name__ == "__main__":
    # Lade die Daten aus der JSON-Datei
    animals_data = load_data("animals_data.json")

    # Drucke die relevanten Informationen
    print_animal_data(animals_data)
