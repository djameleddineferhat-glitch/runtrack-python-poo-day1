# --- CLASSE OPERATION ---
class Operation:
    # JOB 1 : Le Constructeur (__init__)
    # C'est ici qu'on définit les caractéristiques de base de l'objet.
    def __init__(self, nombre1=12, nombre2=3):
        # On utilise 'self' pour dire "cet objet précis".
        # On crée deux attributs (variables d'objet) avec des valeurs par défaut.
        self.nombre1 = nombre1 #
        self.nombre2 = nombre2 #

    # JOB 3 : La Méthode addition()
    # Une méthode est une fonction qui appartient à la classe.
    def addition(self):
        # On récupère les valeurs de l'objet via 'self' pour les additionner.
        resultat = self.nombre1 + self.nombre2
        # On affiche le résultat directement comme demandé.
        print(f"Le résultat de l'addition est : {resultat}")

# --- UTILISATION ---

# Création de l'objet (Instanciation)
mon_operation = Operation() #

# JOB 1 : Affichage de l'objet lui-même
# Cela montre l'identifiant technique de l'objet en mémoire.
print(mon_operation) #

#JOB 2 : Affichage des attributs individuels
# On accède aux données "cachées" dans l'objet avec le point (.).
print(f"La valeur de nombre1 est : {mon_operation.nombre1}")
print(f"La valeur de nombre2 est : {mon_operation.nombre2}")

#JOB 3 : Appel de la méthode addition()
# On demande à l'objet d'exécuter son action d'addition.
mon_operation.addition()