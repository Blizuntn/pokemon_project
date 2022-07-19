import requests

url_1 = "https://pokeapi.co/api/v2/pokemon/?limit=1154&offset=0"
r = requests.get(url_1).json()
pokemon_names = []
pokemon_urls = []
pokemon_types = []
pokemon_effects = []
for i in range(100):
    pokemon_names.append(r["results"][i]["name"].title())
    pokemon_urls.append(r["results"][i]["url"])
for i in range(len(pokemon_urls)):
    new_request = requests.get(pokemon_urls[i]).json()
    pokemon_types.append(new_request["types"][0]["type"]["name"].title())
for i in range(1, len(pokemon_urls) + 1):
    url_4 = f"https://pokeapi.co/api/v2/ability/{i}/"
    r_4 = requests.get(url_4).json()
    for i in r_4["effect_entries"]:
        if i["language"]["name"] == "en":
            pokemon_effects.append(i["short_effect"])

pokemon_data = list(zip(pokemon_names, pokemon_types, pokemon_effects))
