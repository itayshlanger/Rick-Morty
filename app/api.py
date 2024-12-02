from flask import Flask, jsonify
import csv

app = Flask(__name__)

# Load data from CSV
characters = []
with open('rick_and_morty_characters.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        characters.append(row)

@app.route('/characters', methods=['GET'])
def get_characters():
    return jsonify(characters)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
