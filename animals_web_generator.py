import data_fetcher

def generate_html(animal_data, animal_name):
    html_content = """
    <html>
    <head><title>Animal Information</title></head>
    <body>
    <h1>Animal Information</h1>
    """

    if animal_data:
        for animal in animal_data:
            html_content += f"<h2>{animal['name']}</h2>"
            html_content += f"<p><strong>Taxonomy:</strong> {animal['taxonomy']}</p>"
            html_content += f"<p><strong>Locations:</strong> {', '.join(animal['locations'])}</p>"
            html_content += f"<p><strong>Characteristics:</strong> {animal['characteristics']}</p>"
    else:
        html_content += f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"

    html_content += "</body></html>"

    # Save the HTML file
    with open("animals.html", "w") as file:
        file.write(html_content)
    print("The website was successfully generated in the file animals.html.")


animal_name = input("Please enter an animal: ")
# Fetch the data from the data fetcher
animal_data = data_fetcher.fetch_data(animal_name)
# Generate the website using the fetched data
generate_html(animal_data, animal_name)
