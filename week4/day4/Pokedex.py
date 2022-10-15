import requests as r
import random
import time

class Pokedex():
    pokedata = []

    # This function exists in case you'd like to quickly add pokemon to your pokedex.

    def fillPokedex(self):
        for i in range(5):
            random_pokemon_id = random.randint(1, 300)
            self.addPokemon(random_pokemon_id)
            # url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}'
            # response = r.get(url)
            # if not response.ok:
            #     return "Error!"
            # data = response.json()
            # pokedict = {}
            # pokename = data['name']
            # pokedict[pokename] = {
            #     'abilities': [ability['ability']['name'] for ability in data['abilities']],
            #     'base_exp': data['base_experience'],
            #     'f_shiny': data['sprites']['front_shiny']
            # }
            # self.pokedata.append(pokedict)

    def addPokemon(self, pokemon):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = r.get(url)
        if not response.ok:
            return "Error!"
        data = response.json()
        pokedict = {}
        pokename = data['name']
        pokedict[pokename] = {
            'abilities': [ability['ability']['name'] for ability in data['abilities']],
            'base_exp': data['base_experience'],
            'f_shiny': data['sprites']['front_shiny']
        }
        self.pokedata.append(pokedict)

    def showPokemon(self, pokemon, stats):
        print(f'Pokemon name: {stats.capitalize()}\n')
        print("\u0332".join("Abilities: "))
        for i in pokemon[stats]['abilities']:
            print(i.capitalize())
        print("\u0332".join("Base-experience:"), pokemon[stats]['base_exp'])
        print("\u0332".join("Front-shiny:"), pokemon[stats]['f_shiny'] + "\n")

    def showPokedex(self):
        for pokemon in self.pokedata:
            for stats in pokemon.keys():
                self.showPokemon(pokemon, stats)

    def catchPokemon(self):
        pokemon = input("Enter the Pokemon you'd like to catch: ").lower()
        chances = [True, False, False]
        result = random.choice(chances)
        print("wriggle..")
        time.sleep(2)
        print("wriggle...")
        time.sleep(2)
        if result:
            self.addPokemon(pokemon)
            print(f'{pokemon.capitalize()} was caught!')
            return
        print(f'{pokemon.capitalize()} escaped!')
        # url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        # response = r.get(url)
        # if not response.ok:
        #     return "Error!"
        # data = response.json()
        # pokedict = {}
        # pokedict[pokemon] = {
        #     'abilities': [ability['ability']['name'] for ability in data['abilities']],
        #     'base_exp': data['base_experience'],
        #     'f_shiny': data['sprites']['front_shiny']
        # }
        # self.pokedata.append(pokedict)

p1 = Pokedex()
print(len(p1.pokedata))
# p1.fillPokedex()
p1.catchPokemon()
print(len(p1.pokedata))