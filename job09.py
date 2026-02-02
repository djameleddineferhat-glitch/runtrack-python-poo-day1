class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        # Formule : HT + (HT * TVA / 100)
        return self.prixHT * (1 + self.TVA / 100)

    # Getters : Pour récupérer les infos à l'extérieur
    def getNom(self): return self.nom
    def getPrixHT(self): return self.prixHT
    def getTVA(self): return self.TVA

    # Setters : Pour modifier les infos
    def setNom(self, nom): self.nom = nom
    def setPrixHT(self, prix): self.prixHT = prix

    def afficher(self):
        # On retourne une string au lieu de faire un print
        return f"Produit: {self.nom} | HT: {self.prixHT}€ | TVA: {self.TVA}% | TTC: {self.CalculerPrixTTC():.2f}€"

# Test du Job 9
p1 = Produit("MacBook", 1200, 20)
p2 = Produit("iPhone", 800, 20)

# Affichage initial via la méthode qui retourne une chaîne
print(p1.afficher())
print(p2.afficher())

# Modifications demandées
p1.setNom("MacBook Pro 16")
p1.setPrixHT(2500)
p2.setNom("iPhone 15 Pro")
p2.setPrixHT(1100)

# Affichage des nouveaux prix
print("\n--- Après modifications ---")
print(f"Nouveau prix {p1.getNom()} : {p1.CalculerPrixTTC()}€")
print(f"Nouveau prix {p2.getNom()} : {p2.CalculerPrixTTC()}€")