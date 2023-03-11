class Pokemon:
    def __init__(self, nom, type, defense, puissance_attaque, point_de_vie):
        self._nom = nom
        self._type = type
        self.defense = defense
        self.puissance_attaque = puissance_attaque
        self.point_de_vie = point_de_vie

    @property
    def nom(self):
        return self._nom

    @property
    def point_de_vie(self):
        return self._point_de_vie

    @point_de_vie.setter
    def point_de_vie(self, value):
        self._point_de_vie = value

    def afficher_informations(self):
        print("Nom: {}\nType: {}\nPoints de vie: {}\nDéfense: {}\nPuissance d'attaque: {}\n"
              .format(self.nom, self._type, self.point_de_vie, self.defense, self.puissance_attaque))

class PokemonNormal(Pokemon):
    def __init__(self, nom, defense=5, puissance_attaque=10, point_de_vie=100):
        super().__init__(nom, "Normal", defense, puissance_attaque, point_de_vie)

class PokemonFeu(Pokemon):
    def __init__(self, nom, defense=4, puissance_attaque=12, point_de_vie=80):
        super().__init__(nom, "Feu", defense, puissance_attaque, point_de_vie)

class PokemonEau(Pokemon):
    def __init__(self, nom, defense=6, puissance_attaque=8, point_de_vie=120):
        super().__init__(nom, "Eau", defense, puissance_attaque, point_de_vie)

class PokemonTerre(Pokemon):
    def __init__(self, nom, defense=8, puissance_attaque=6, point_de_vie=150):
        super().__init__(nom, "Terre", defense, puissance_attaque, point_de_vie)