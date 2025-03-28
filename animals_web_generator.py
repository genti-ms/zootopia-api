import json


def load_data(file_path):
    """Lädt eine JSON-Datei"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_info(animals):
    """Generiert HTML-Inhalt für jedes Tier im neuen Format"""
    output = ''  # leere Zeichenkette, die später mit den Tierinformationen gefüllt wird
    for animal in animals:
        animal_info = "<li class='cards__item'>"  # Beginn des <li>-Tags

        if "name" in animal:
            animal_info += f"<div class='card__title'>{animal['name']}</div>\n"

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            animal_info += "<p class='card__text'>"

            if "diet" in characteristics:
                animal_info += f"<strong>Diet:</strong> {characteristics['diet']}<br/>\n"

            if "locations" in animal and animal["locations"]:
                animal_info += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

            if "type" in characteristics:
                animal_info += f"<strong>Type:</strong> {characteristics['type']}<br/>\n"

            animal_info += "</p>"  # Ende des <p>-Tags

        animal_info += "</li>"  # Ende des <li>-Tags
        output += animal_info  # Füge das Tier der Gesamtliste hinzu

    return output


def create_html(template_path, animals_data):
    """Erstellt eine neue HTML-Datei basierend auf der Vorlage und den Tierdaten"""
    # Lese die Vorlage
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    # Generiere den HTML-Inhalt mit den Tierdaten
    animals_info = generate_animal_info(animals_data)

    # Ersetze den Platzhalter __REPLACE_ANIMALS_INFO__ durch die generierten Tierinformationen
    updated_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info)

    # Schreibe den neuen HTML-Inhalt in eine Datei
    with open('animals.html', 'w') as output_file:
        output_file.write(updated_html)

    # Bestätigungsmeldung
    print("HTML file 'animals.html' created successfully!")


if __name__ == "__main__":
    # Lade die Tierdaten aus der JSON-Datei
    animals_data = load_data("animals_data.json")

    # Erstelle die HTML-Datei mit den Tierdaten
    create_html('animals_template.html', animals_data)
