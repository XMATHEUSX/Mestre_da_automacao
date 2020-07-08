import json
from pathlib import Path

arq_pokemon = Path('pikachu\\pikachu.json').read_text()
arq_pokemon_json = json.loads(arq_pokemon)
print(arq_pokemon_json["abilities"][1]['ability']['name'])
