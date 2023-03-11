import json
import random
from combat import Combat
from pokemon import PokemonNormal, PokemonFeu, PokemonEau, PokemonTerre

class Pokedex:
    def __init__(self):
        with open('pokedex.json', 'r') as f:
            self.pokemon = json.load(f)

    def print_pokemon(self):
        for p in self.pokemon:
            pokemon_type = p["type"]
            if pokemon_type == "Normal":
                pokemon = PokemonNormal(p["nom"])
            elif pokemon_type == "Feu":
                pokemon = PokemonFeu(p["nom"])
            elif pokemon_type == "Eau":
                pokemon = PokemonEau(p["nom"])
            elif pokemon_type == "Terre":
                pokemon = PokemonTerre(p["nom"])

            print(f'{pokemon.nom} ({pokemon_type}) - {pokemon.defense} Defense - {pokemon.puissance_attaque} Attaque - {pokemon.point_de_vie} HP')

    def add_pokemon(self, nom, p_type):
        if p_type == "Normal":
            pokemon = PokemonNormal(nom)
        elif p_type == "Feu":
            pokemon = PokemonFeu(nom)
        elif p_type == "Eau":
            pokemon = PokemonEau(nom)
        elif p_type == "Terre":
            pokemon = PokemonTerre(nom)

        self.pokemon.append({"nom": pokemon.nom, "type": p_type})
        with open('pokedex.json', 'w') as f:
            json.dump(self.pokemon, f)

    def get_pokemon(self, nom):
        for p in self.pokemon:
            if p["nom"] == nom:
                pokemon_type = p["type"]
                if pokemon_type == "Normal":
                    return PokemonNormal(p["nom"])
                elif pokemon_type == "Feu":
                    return PokemonFeu(p["nom"])
                elif pokemon_type == "Eau":
                    return PokemonEau(p["nom"])
                elif pokemon_type == "Terre":
                    return PokemonTerre(p["nom"])
        return None

pokedex = Pokedex()

def add_pokemon():
    nom = input('Enter the nom of the Pokemon: ')
    p_type = input('Enter the type of the Pokemon: ')
    pokedex.add_pokemon(nom, p_type)
    print(f'{nom} has been added to the Pokedex!')

def view_pokedex():
    pokedex.print_pokemon()

while True:
    print('\nWelcome to the Pokemon Game!')
    print('Please select an option:')
    print('1. Start a game')
    print('2. Add a Pokemon to the Pokedex')
    print('3. View your Pokedex')

    choice = input('Enter your choice: ')

    if choice == '1':
        print("Choose two Pokémons for the battle:")
        pokemon1 = input("Pokemon 1: ")
        pokemon2 = random.choice([p["nom"] for p in pokedex.pokemon])
        if pokemon1 not in [p["nom"] for p in pokedex.pokemon]:
            print("Error: Invalid Pokemon")
        else:
            pokemon1 = pokedex.get_pokemon(pokemon1)
            pokemon2 = pokedex.get_pokemon(pokemon2)
            combat = Combat(pokemon1, pokemon2, pokedex)
            combat.jouer()
    elif choice == '2':
        add_pokemon()
    elif choice == '3':
        view_pokedex()
    else:
        print('Invalid choice, please try again.')