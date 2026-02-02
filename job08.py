import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"--- Infos du Cercle ---")
        print(f"Rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference():.2f}")
        print(f"Aire : {self.aire():.2f}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return self.rayon * 2

# Test du Job 8 avec deux cercles
c1 = Cercle(4)
c2 = Cercle(7)

c1.afficherInfos()
c2.afficherInfos()