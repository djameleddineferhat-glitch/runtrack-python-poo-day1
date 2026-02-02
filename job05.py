class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        # Affiche les deux coordonnées
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La valeur de X est : {self.x}")

    def afficherY(self):
        print(f"La valeur de Y est : {self.y}")

    def changerX(self, nouveau_x):
        # On modifie l'attribut x avec la nouvelle valeur reçue
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        self.y = nouveau_y

# Test
p = Point(5, 10)
p.afficherLesPoints()
p.changerX(20) # On change x
p.afficherX()    # Vérification