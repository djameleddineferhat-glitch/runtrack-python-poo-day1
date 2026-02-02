class Personne:
    # Le constructeur prend maintenant des arguments (nom, prenom)
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    # Méthode pour retourner une chaîne de caractères
    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"

# Instanciation de plusieurs objets avec des valeurs différentes
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupont", "Jean")

# Appel de la méthode et affichage
print(personne1.SePresenter())
print(personne2.SePresenter())