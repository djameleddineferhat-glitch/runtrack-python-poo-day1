class Operation:
    # Le constructeur : c'est la fonction qui prépare l'objet
    def __init__(self, nombre1=12, nombre2=3):
        # 'self' représente l'objet que l'on est en train de créer.
        # On lui attache deux "étiquettes" (attributs) avec des valeurs par défaut.
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# On crée l'objet (on appelle ça "instancier")
# ma_premiere_classe devient une instance réelle de la classe Operation.
classe = Operation()

# On affiche l'objet lui-même
print(classe)