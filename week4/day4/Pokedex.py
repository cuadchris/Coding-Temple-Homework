import requests as r
import random
import time
import sys

class Pokedex():
    pokedata = []

    # This function exists in case you'd like to quickly add pokemon to your pokedex. It takes an
    # integer for how many you'd like to add.

    def fillPokedex(self, amount):
        for i in range(amount):
            random_pokemon_id = random.randint(1, 300)
            self.addPokemon(random_pokemon_id)

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
        # You only have a 33% chance to actually catch the Pokemon you want. Sorry!, lol.
        chances = [True, False, False]
        result = random.choice(chances)
        self.pokePrint("You used POKe´BALL!\n", .08)
        time.sleep(1.5)
        print("wriggle..")
        time.sleep(2)
        print("wriggle...")
        time.sleep(2)
        if result:
            self.addPokemon(pokemon)
            self.pokePrint(f'{pokemon.capitalize()} was caught!\n', .03)
            time.sleep(1.5)
            self.pokePrint("Here are the stats:\n", .03)
            self.showPokemon(self.pokedata[-1], pokemon)
            return
        self.pokePrint(f'{pokemon.capitalize()} escaped!\n', .03)

    # That classic Gameboy Pokemon text. Use the speed argument to play around!
    def pokePrint(self, string, speed):
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)

pokedex = Pokedex()
# pokedex.fillPokedex(5) < Use this to quick add.
# p1.catchPokemon() < Use this to catch a Pokemon!
# pokedex.showPokedex() < Show off your Codex!