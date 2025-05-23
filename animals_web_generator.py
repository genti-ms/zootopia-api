import data_fetcher

def format_dict_to_html(d):
    """
    Converts a dictionary to an HTML unordered list.

    Args:
        d (dict): Dictionary to convert.

    Returns:
        str: HTML string representing the dictionary as a <ul> list.
    """
    if not isinstance(d, dict):
        return str(d)
    html = "<ul>"
    for key, value in d.items():
        html += f"<li><strong>{key}:</strong> {value}</li>"
    html += "</ul>"
    return html

def generate_html(animal_data, animal_name):
    """
    Generates an HTML page based on animal data and writes it to 'animals.html'.

    Args:
        animal_data (list): A list of dictionaries containing animal information.
        animal_name (str): The name of the animal queried by the user.
    """
    # Read template file
    with open("animals_template.html", "r") as f:
        template = f.read()

    animal_cards_html = ""

    if animal_data:
        for animal in animal_data:
            name = animal.get('name', 'Unknown')
            taxonomy = format_dict_to_html(animal.get('taxonomy', {}))
            characteristics = format_dict_to_html(animal.get('characteristics', {}))
            locations = animal.get('locations', [])
            locations_str = ', '.join(locations) if locations else 'No locations available'

            card_html = f"""
            <li class="cards__item">
              <h2 class="card__title">{name}</h2>
              <p><strong>Taxonomy:</strong> {taxonomy}</p>
              <p><strong>Locations:</strong> {locations_str}</p>
              <p><strong>Characteristics:</strong> {characteristics}</p>
            </li>
            """
            animal_cards_html += card_html
    else:
        animal_cards_html = f'<h2 style="color: red;">❌ The animal "{animal_name}" does not exist or was not found.</h2>'

    # Replace placeholder with generated content
    output_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_cards_html)

    with open("animals.html", "w") as f:
        f.write(output_html)

    print("✅ The website was successfully generated in animals.html.")

def main():
    """
    Main function that prompts user input, fetches animal data, and generates the HTML page.
    """
    animal_name = input("Please enter an animal: ").strip()
    if not animal_name:
        print("❌ No animal name entered. Website was not generated.")
        return

    animal_data = data_fetcher.fetch_data(animal_name)
    generate_html(animal_data, animal_name)

if __name__ == "__main__":
    main()
