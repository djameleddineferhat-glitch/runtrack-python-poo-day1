class Personnage:
    def __init__(self, x, y):
        # Initialisation de la position de départ (x, y)
        self.x = x
        self.y = y

    # Méthodes de déplacement
    def gauche(self): self.x -= 1
    def droite(self): self.x += 1
    def haut(self):   self.y -= 1
    def bas(self):    self.y += 1

    def position(self):
        # Retourne les coordonnées sous forme de tuple
        return (self.x, self.y)

# Test du Job 7
joueur = Personnage(5, 5)
joueur.droite()
joueur.bas()
print(f"Position actuelle du joueur : {joueur.position()}")