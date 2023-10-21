import requests
from bs4 import BeautifulSoup
import json

def extract_song(url):

    # Send an HTTP GET request
    response = requests.get(url)

    print(response.status_code)

    # Check if the request was successful
    if response.status_code == 200:
    
        # Analizza il contenuto HTML della pagina
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trova l'elemento <div> con la classe "js-store"
        div_element = soup.find('div', class_='js-store')

        # Estrai il valore dell'attributo "data-content"
        data_content = div_element['data-content']

        # Gestisci il valore come JSON
        json_data = json.loads(data_content)
        
        #print_first_level_keys(json_data['store'])
        song_name = json_data['store']['page']['data']['tab']['song_name']
        print(song_name)
        artist_name = json_data['store']['page']['data']['tab']['artist_name']
        print(artist_name)
        rating = json_data['store']['page']['data']['tab']['rating']
        print(rating)
        votes = json_data['store']['page']['data']['tab']['votes']
        print(votes)
        content = json_data['store']['page']['data']['tab_view']['wiki_tab']['content']
        
        print(content)
        
        return {'song_name':song_name, 'artist_name':artist_name, 'votes':votes, 'rating':rating, 'content':content}
        #print(json_data['store']['page']['data']['tab_view'])

        #target_word = "55"
        #result = search_word_in_string(response.text, target_word)
        #result = find_element_by_path_with_keyword(json_data , target_word)
        #print(result)
        #path = find_path_to_element(json_data, 'rating')
        #print(path)
        
        #if result:
        #    print(result)
        #else:
        #    print(f"La parola '{target_word}' non è stata trovata nell'oggetto JSON.")
        
        
        # Ora puoi lavorare con json_data come un dizionario Python
        # print(json_data)
    else:
        print("Errore nella richiesta HTTP")
        return {}

def search_word_in_string(input_string, target_word):
    index = input_string.find(target_word)
    if index != -1:
        print(f"'{target_word}' trovata nella stringa all'indice {index}.")
    else:
        print(f"'{target_word}' non trovata nella stringa.")

def find_element_by_path_with_keyword(json_data, keyword, path=""):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            current_path = f"{path}.{key}" if path else key
            if isinstance(value, (dict, list)):
                result = find_element_by_path_with_keyword(value, keyword, current_path)
                if result:
                    return result
            elif isinstance(value, str) and keyword in current_path:
                return value
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            current_path = f"{path}[{i}]"
            if isinstance(item, (dict, list)):
                result = find_element_by_path_with_keyword(item, keyword, current_path)
                if result:
                    return result
    return None

def find_path_to_element(json_data, target_element, current_path=""):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            current_key_path = f"{current_path}.{key}" if current_path else key
            if key == target_element:
                return current_key_path
            if isinstance(value, (dict, list)):
                result = find_path_to_element(value, target_element, current_key_path)
                if result:
                    return result
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            current_item_path = f"{current_path}[{i}]"
            if isinstance(item, (dict, list)):
                result = find_path_to_element(item, target_element, current_item_path)
                if result:
                    return result
    return None







def print_first_level_keys(json_data):
    if isinstance(json_data, dict):
        keys = list(json_data.keys())
        print(keys)    

import json

def process_json_file(input_file, output_file):
    try:
        # Leggi il JSON dal file di input
        with open(input_file, 'r') as json_file:
            json_data = json.load(json_file)

        # Copia l'oggetto JSON originale
        new_json = json_data.copy()

        # Naviga fino al campo "links" se esiste
        for artist in new_json['artists']:
            for song in artist['songs']:
                if song.get("data") is None:
                    song["data"] = []
                for link in song['links']:
                    song["data"].append(extract_song(link))
                
        # Scrivi il JSON aggiornato nel file di output
        with open(output_file, 'w') as new_json_file:
            json.dump(new_json, new_json_file, indent=4)

        print("JSON aggiornato e scritto in", output_file)

    except Exception as e:
        print("Si è verificato un errore:", str(e))

# Esempio di utilizzo
input_file = "songs_links.json"
output_file = "songs_data.json"
process_json_file(input_file, output_file)

        
# Esempio di utilizzo
#url = 'https://tabs.ultimate-guitar.com/tab/the-beatles/i-want-to-hold-your-hand-chords-17419'
#url = 'https://tabs.ultimate-guitar.com/tab/the-beatles/she-loves-you-chords-17355'
#result = extract_song(url)


