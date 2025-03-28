import json


# Function to load the JSON file
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load the data from the JSON file
animals_data = load_data('animals_data.json')

# Step 1: Read the content of the template HTML file
with open('animals_template.html', 'r') as template_file:
    template_content = template_file.read()

# Step 2: Generate a string with the animals' data
output = ''  # Define an empty string
for animal in animals_data:
    # Start with the Name
    output += f"Name: {animal['name']}\n"

    if 'characteristics' in animal:
        if 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n"

    # Print Location (first location in the list)
    if 'locations' in animal and animal['locations']:
        output += f"Location: {animal['locations'][0]}\n"


# Step 3: Replace __REPLACE_ANIMALS_INFO__ in the template with the output
final_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 4: Write the new HTML content to a new file
with open('animals.html', 'w') as output_file:
    output_file.write(final_content)

print("HTML file generated successfully as 'animals.html'.")
