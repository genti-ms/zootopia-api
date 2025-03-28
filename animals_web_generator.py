import json


# Function to load the JSON file
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load the data from the JSON file
animals_data = load_data('animals_data.json')

# Read the content of the template HTML file
with open('animals_template.html', 'r') as template_file:
    template_content = template_file.read()

# Generate an HTML list with the animals' data
output = '<ul class="cards">\n'  # Start the unordered list
for animal in animals_data:
    output += '<li class="cards__item">\n'
    output += f"Name: {animal['name']}<br/>\n"

    if 'characteristics' in animal:
        if 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"

    if 'locations' in animal and animal['locations']:
        output += f"Location: {animal['locations'][0]}<br/>\n"

    output += '</li>\n'
output += '</ul>'  # Close the unordered list

# Replace placeholder in the template with the generated HTML
final_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# Write the new HTML content to a file
with open('animals.html', 'w') as output_file:
    output_file.write(final_content)

print("HTML file generated successfully as 'animals.html'.")
