import requests
import csv

# API endpoint
url = "https://rickandmortyapi.com/api/character/"

# Query parameters
params = {
    "species": "Human",
    "status": "Alive",
    "origin": "Earth"
}

# Send request to the API and save data
response = requests.get(url, params=params)
characters = response.json()['results']

# Prepare data for CSV
data = []
for character in characters:
    name = character['name']
    location = character['location']['name']
    image_link = character['image']
    data.append([name, location, image_link])

# Write data to CSV file
csv_file = "./rick_and_morty_characters.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Location', 'Image'])
    writer.writerows(data)

print(f"Data written to {csv_file}")
