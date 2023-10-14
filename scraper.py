import requests
import re

from bs4 import BeautifulSoup
from urllib.parse import quote

def extract_links_with_prefix(url, param_value, prefix):
    """
    Extract links from a web page accessed via a URL with a specific parameter, and filter for links
    that start with a given prefix.

    Args:
        url (str): The URL with the parameter.
        param_value (str): The value of the parameter.
        prefix (str): The prefix to filter the links.

    Returns:
        list: A list of URLs that match the specified prefix.
    """
    print("url: "+url)

    print("param_value: "+param_value)

    
    # Construct the URL with the parameter
    full_url = url+"?page=1&type=300&title="+quote(param_value)

    print("full_url: "+full_url)

    # Send an HTTP GET request
    response = requests.get(full_url)

    print(response.status_code)

    # Check if the request was successful
    if response.status_code == 200:
        
        # Definisci il pattern regex per trovare le occorrenze desiderate
        pattern = r'https://tabs\.ultimate-guitar\.com/tab/.*?&quot;'

        # Trova tutte le corrispondenze nel testo
        matching_urls = re.findall(pattern, response.text)
        filtered_list = [string for string in matching_urls if "-chords-" in string and "/misc-mashups/" not in string]

        clean_matching_urls = [match[:-6] for match in filtered_list]

        return clean_matching_urls
    else:
        print("HTTP request failed")
        return []

import json

def extract_songs_from_json_file(file_path):
    """
    Extract a list of songs from a JSON file, distinguishing the song name, artist, and year.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of dictionaries containing song details (name, artist, and year).
    """
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Initialize a list for songs
        songs = []

        # Extract information
        for decade, songs_in_decade in data.items():
            for song_info in songs_in_decade:
                parts = song_info.split(" - ")
                if len(parts) == 2:
                    song_name, details = parts
                    artist, year = details.split(" (")
                    year = year[:-1]  # Remove the closing parenthesis
                    songs.append({
                        "Song Name": song_name,
                        "Artist": artist,
                        "Year": year,
                    })

        return songs
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

file_path = "songs_names.json"  # Replace with the path to your JSON file
songs = extract_songs_from_json_file(file_path)

ultimate_guitar_url = "https://www.ultimate-guitar.com/search.php"

prefix = "https://tabs.ultimate-guitar.com/tab/"

# Inizializza una struttura dati vuota
data = {"artists": []}

# Funzione per aggiungere le informazioni alla struttura dati esistente
def add_info(data, info):
    # Trova l'artista nella struttura dati esistente o aggiungilo se non esiste
    artist_data = next((artist for artist in data["artists"] if artist["name"] == info["artist"]), None)
    if artist_data is None:
        artist_data = {"name": info["artist"], "songs": []}
        data["artists"].append(artist_data)

    # Aggiungi la canzone e la lista di link all'artista
    song_data = {"name": info["song"], "year": info["year"], "links": info["links"]}
    artist_data["songs"].append(song_data)

# Print the list of songs
for song in songs:
    song_name = song["Song Name"]
    artist = song["Artist"]
    year = song["Year"]
    # Dividi la stringa in base a "ft."
    parts = artist.split("ft.", 1)
    # Prendi solo la parte prima di "ft."
    artist = parts[0].strip()
    formatted_name = f"{song_name} {artist}".replace("?", "").replace("&", "").replace(" ", "+")
    remove_brackets = re.sub(r'\([^)]*\)', '', formatted_name)

    matching_urls = extract_links_with_prefix(ultimate_guitar_url, remove_brackets, prefix)
    # Print the matching URLs
    for url in matching_urls:
        print(url)
    add_info(data, {"artist": artist,"song": song_name, "year": year, "links": matching_urls})
# Example usage:

# Salva i dati in un file JSON
with open('songs_links.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data saved to music_data.json")

