import data_fetcher

def generate_html(animal_data, animal_name):
    html_content = f"""
    <html>
    <head><title>Animal Information</title></head>
    <body>
    <h1>Animal Information for {animal_name}</h1>
    """

    if animal_data:
        for animal in animal_data:
            html_content += f"<h2>{animal.get('name', 'Unknown')}</h2>"

            taxonomy = animal.get('taxonomy', 'No taxonomy data available')
            locations = animal.get('locations', [])
            characteristics = animal.get('characteristics', 'No characteristics available')

            locations_str = ', '.join(locations) if locations else 'No locations available'

            html_content += f"<p><strong>Taxonomy:</strong> {taxonomy}</p>"
            html_content += f"<p><strong>Locations:</strong> {locations_str}</p>"
            html_content += f"<p><strong>Characteristics:</strong> {characteristics}</p>"
    else:
        # Show a nice message if no data is found
        html_content += f"<h2 style='color: red;'>❌ The animal \"{animal_name}\" does not exist or was not found.</h2>"

    html_content += """
    </body>
    </html>
    """

    with open("animals.html", "w") as file:
        file.write(html_content)
    print(f"✅ The website was successfully generated in animals.html.")

# Main 
if __name__ == "__main__":
  animal_name = input("Please enter an animal: ").strip()

  if not animal_name:
     print("❌ No animal name entered. Website was not generated.")
  else:
      animal_data = data_fetcher.fetch_data(animal_name)

      if animal_data:
          generate_html(animal_data, animal_name)
      else:
          print(f"❌ No data found for \"{animal_name}\". Website was not generated.")
 