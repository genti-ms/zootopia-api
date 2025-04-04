import data_fetcher

def generate_html(animal_data, animal_name):
    # Start of the HTML content without CSS
    html_content = f"""
    <html>
    <head><title>Animal Information</title></head>
    <body>
    <h1>Animal Information for {animal_name}</h1>
    """

    # Check if animal data exists and process accordingly
    if animal_data:
        for animal in animal_data:
            html_content += f"<h2>{animal.get('name', 'Unknown')}</h2>"

            # Handle missing or incomplete information safely
            taxonomy = animal.get('taxonomy', 'No taxonomy data available')
            locations = animal.get('locations', [])
            characteristics = animal.get('characteristics', 'No characteristics available')


            locations_str = ', '.join(locations) if locations else 'No locations available'


            html_content += f"<p><strong>Taxonomy:</strong> {taxonomy}</p>"
            html_content += f"<p><strong>Locations:</strong> {locations_str}</p>"
            html_content += f"<p><strong>Characteristics:</strong> {characteristics}</p>"
    else:
        html_content += f"<h2>The animal \"{animal_name}\" doesn't exist or was not found.</h2>"

    html_content += """
    </body>
    </html>
    """

    # Save the HTML 
    with open("animals.html", "w") as file:
        file.write(html_content)
    print(f"The website was successfully generated in the file animals.html.")

# Main 
if __name__ == "__main__":
    animal_name = input("E enter an animal: ")
    animal_data = data_fetcher.fetch_data(animal_name)
    generate_html(animal_data, animal_name)
