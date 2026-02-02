class Animal:
    def __init__(self):
        # Initialisation par défaut selon l'énoncé
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        # Ajoute 1 à l'âge actuel
        self.age += 1

    def nommer(self, nom):
        # Assigne le nom passé en paramètre à l'attribut prenom
        self.prenom = nom

# 1. Création et affichage de l'âge initial
mon_animal = Animal()
print(f"L'âge de l'animal {mon_animal.age} ans")

# 2. On fait vieillir l'animal
mon_animal.vieillir()
print(f"L'âge de l'animal {mon_animal.age} ans")

# 3. On lui donne un nom
mon_animal.nommer("Luna")
print(f"L'animal se nomme {mon_animal.prenom}")