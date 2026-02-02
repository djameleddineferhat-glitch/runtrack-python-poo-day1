import json
import os

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def to_dict(self):
        # Convertit l'objet en dictionnaire pour le format JSON
        return {
            "nom": self.nom,
            "prixHT": self.prixHT,
            "TVA": self.TVA,
            "prixTTC": self.CalculerPrixTTC()
        }

# 1. Création d'une liste de produits
inventaire = [
    Produit("Laptop", 1000, 20),
    Produit("Souris", 20, 20),
    Produit("Clavier", 50, 20)
]

# 2. Sauvegarde dans un fichier JSON
def sauvegarder_stock(liste_produits, filename="stock.json"):
    # On transforme chaque objet Produit en dictionnaire
    data = [p.to_dict() for p in liste_produits]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ Stock sauvegardé dans {filename}")

# 3. Lecture et affichage du fichier JSON
def charger_et_afficher(filename="stock.json"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            stock_charge = json.load(f)
            print("\n--- Contenu du Stock (JSON) ---")
            for p in stock_charge:
                print(f"Nom: {p['nom']} | Prix TTC: {p['prixTTC']}€")
    else:
        print("Fichier introuvable.")

# --- Exécution ---
sauvegarder_stock(inventaire)
charger_et_afficher()