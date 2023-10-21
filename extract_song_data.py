import json
import re
from collections import Counter

def read_json_scraped_file(input_file, output_file):
    # Leggi il JSON dal file di input
    with open(input_file, 'r') as json_file:
        json_data = json.load(json_file)

    songs_json = {"songs": []}

    # Naviga fino al campo "links" se esiste
    for artist in json_data['artists']:
        for song in artist['songs']:
            chosenContent = ""
            maxVotes = 0
            year = song['year']
            for data in song['data']:
                if 'votes' in data and data['votes']> maxVotes:
                    maxVotes = data['votes']
                    chosenContent = data['content']
                    artist = data['artist_name']
                    song = data['song_name']
            
            if chosenContent != "":
                songs_json["songs"].append({'artist':artist, 'song':song, 'year':year, 'structure':extractSongData(chosenContent)})
            
    
    
    # Scrivi il JSON aggiornato nel file di output
    with open(output_file, 'w') as new_json_file:
        json.dump(songs_json, new_json_file, indent=4)

    print("JSON aggiornato e scritto in", output_file)
    
def extractSongData(context):
    song_structure_pattern = r'^\[[^\[\]]*\]$'
    structure_pattern = r'\[(Intro|Hook|Pre-Hook|Chorus|Сhorus|Verse|Bridge|Outro|Ending|.*Solo|Instrumental|Coda|Middle|Interlude|Break|Pre Chorus|Prechorus|Pre-Chorus|Pre-Bridge|Post-Chorus|Final Chorus|refrain).*?\]'
    lines = context.split('\n')
    # Inizializza una lista per le righe valide
    valid_parts = []
    chords = []

    # Controlla ciascuna riga utilizzando il pattern RegEx
    curr_part = None
    prev_content = ""
    lyrics = ""
    for line in lines:
        #print(line)
        line = line.strip()
        
        if re.match(song_structure_pattern, line):
            if re.match(structure_pattern, line, re.IGNORECASE):
                if curr_part is not None:                    
                    chords_list = extract_chords(prev_content)
                    lyrics= lyrics + (extract_lyrics(prev_content))
                    pattern = elimina_pattern_contenuti([item[0] for item in extract_patterns(chords_list)])
                    chords.append({'part':curr_part, 'chord_progressions':chords_list})
                    prev_content = ""
                curr_part = line[1:-1].split(":", 1)[0]
                valid_parts.append(curr_part)                
            else:            
                curr_part = None
        elif curr_part is not None:
            prev_content=prev_content + line
    
    if curr_part is not None:
        chords_list = extract_chords(prev_content)
        lyrics= lyrics + (extract_lyrics(prev_content))
        pattern = elimina_pattern_contenuti([item[0] for item in extract_patterns(chords_list)])
        chords.append({'part':curr_part, 'chord_progressions': chords_list})

    # Stampa le righe valide
    #for line in valid_lines:
     #   print(line)

    stop_words = [
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
        "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are",
        "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
        "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
        "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up",
        "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
        "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor",
        "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will,", "just", "don", "should", "now", "m", "ll", "re", "doesn","ve","d","didn","cos","n","ain","wouldn", "em","isn", "oh", "uh","til","ah","yeah", "hey", "let", "ooh", "mmm", "eh"
    ]
    
    return {'structure':valid_parts, 'music':chords, 'lyrics': re.sub(r'\s+', ' ', lyrics), 'words_occurrences':estrai_parole_e_occorrenze(lyrics, stop_words), 'chords_occurrences':extract_all_chords(chords)}

def extract_all_chords(chords):
    result = Counter()  # Initialize a Counter object for the result
    
    for chord in chords:        
        count = Counter(chord['chord_progressions'])  # Count occurrences in the current list
        result += count  # Add the count to the overall result
    
    # Convert the final count into a list of tuples (word, occurrences)
    word_occurrences_list = list(result.items())
    
    return sorted(word_occurrences_list, key=lambda x: x[1], reverse=True)

def extract_chords(text):

    # Definisci il pattern RegEx per corrispondere ai tag [ch]
    pattern = r'\[ch\](.*?)\[/ch\]'

    # Utilizza il modulo re per cercare tutte le corrispondenze nel testo
    matches = re.findall(pattern, text)

    return matches


def extract_patterns(lista):
    pattern_ripetuti = []
    lunghezza_lista = len(lista)

    for lunghezza_pattern in range(1, lunghezza_lista // 2 + 1):
        for i in range(lunghezza_lista - 2 * lunghezza_pattern + 1):
            pattern = lista[i:i + lunghezza_pattern]
            occorrenze = [j for j in range(i + lunghezza_pattern, lunghezza_lista - lunghezza_pattern + 1) if lista[j:j + lunghezza_pattern] == pattern]
            
            if occorrenze:
                occorrenze.append(i)  # Aggiungi anche la posizione iniziale del pattern
                pattern_ripetuti.append((pattern, occorrenze))

    return pattern_ripetuti

def elimina_pattern_contenuti(lista):
    # Ordina la lista per lunghezza decrescente in modo da gestire prima i pattern più lunghi
    lista = sorted(lista, key=lambda x: len(x), reverse=True)
    
    risultato = []

    for pattern in lista:
        # Verifica se il pattern è già stato completamente incluso in un altro pattern
        incluso = False
        for p in risultato:
            if set(pattern).issubset(set(p)):
                incluso = True
                break

        # Se il pattern non è incluso in un altro, lo aggiungi al risultato
        if not incluso:
            risultato.append(pattern)

    return risultato

def remove_tab_from_text(input_string):
    # Dividi la stringa in righe
    lines = input_string.split('\n')

    # Filtra le righe che non iniziano per "E|-"
    filtered_lines = [line for line in lines if not line.startswith("E|-")]

    # Unisci le righe filtrate in una stringa
    output_string = '\n'.join(filtered_lines)
    return output_string

def extract_lyrics(input_string):
    input_string = remove_tab_from_text(input_string)
    # Utilizza un'espressione regolare per estrarre il testo all'interno dei tag [tab]
    tab_text = re.findall(r'\[tab\](.*?)\[/tab\]', input_string, re.DOTALL)

    # Rimuovi il contenuto dei tag [ch] all'interno di [tab]
    for i in range(len(tab_text)):
        text = re.sub(r'\[ch\].*?\[/ch\]', '', tab_text[i])
        if not contiene_tabs(tab_text[i]):
            tab_text[i] = text
        else:
            tab_text[i] = ''

    return ' '+ ' '.join(tab_text).replace("|", "").replace("N.C.", "")+' '

def estrai_parole_e_occorrenze(testo, parole_da_elim):
    # Utilizziamo espressioni regolari per suddividere il testo in parole
    parole = re.findall(r'\w+', testo.lower())  # Converto tutto in minuscolo e trovo le parole

    occorrenze = {}  # Un dizionario per tenere traccia delle occorrenze delle parole

    for parola in parole:
        if parola not in parole_da_elim:
            if parola in occorrenze:
                occorrenze[parola] += 1
            else:
                occorrenze[parola] = 1

    parole_ordinate = sorted(occorrenze.items(), key=lambda x: x[1], reverse=True)

    return parole_ordinate

def contiene_tabs(stringa):
    pattern = r"(e|a|d|g|b)\|--"  # Definiamo il pattern regex da cercare
    match = re.search(pattern, stringa, re.I)  # Cerca il pattern nella stringa
    return match is not None
    
read_json_scraped_file('songs_data.json','songs_content.json')