import requests

def fetch_animal_data(animal_name):
    url = "https://api.api-ninjas.com/v1/animals"
    api_key = "gR/VxO32JnWUv555uz2nQQ==VZUv1hfXQQUH5XMz"

    response = requests.get(
        url,
        params={"name": animal_name},
        headers={"X-Api-Key": api_key}
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def generate_html(animal_data, animal_name):
    html_content = """
    <html>
    <head><title>Animal Info</title></head>
    <body>
    <h1>Animal Information</h1>
    """

    if animal_data:
        for animal in animal_data:
           html_content += f"<h2>{animal.get('name', 'Unbekannt')}</h2>"
           html_content += f"<p><strong>Klassifikation:</strong> {animal.get('classification', 'Nicht verfügbar')}</p>"
           html_content += f"<p><strong>Ernährung:</strong> {animal.get('diet', 'Nicht verfügbar')}</p>"
           html_content += f"<p><strong>Lebenserwartung:</strong> {animal.get('lifespan', 'Nicht verfügbar')}</p>"
           html_content += f"<p><strong>Lebensraum:</strong> {animal.get('habitat', 'Nicht verfügbar')}</p>"

    else:
        html_content += f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"

    html_content += "</body></html>"

    # Save the HTML file
    with open("animals.html", "w") as file:
        file.write(html_content)
    print("Website was successfully generated to the file animals.html.")

# Mainpart
animal_name = input("Enter a name of an animal: ")
animal_data = fetch_animal_data(animal_name)
generate_html(animal_data, animal_name)