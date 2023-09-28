# créer une classe moldu qui a un attribut nom
class Moldu:

    def __init__(self, name):
        self.name = name

#Créer une classe sorcier qui a un attribut maison
#Faire en sorte que la classe sorcier hérite de la classe moldu
class Wizard(Moldu):

    def __init__(self, name, house):
        super().__init__(name)
        self.__house = house

    # Ajouter une méthode lancer_un_sort à la classe Sorcier. La méthode lancer_un_sort() affiche Lancer un sort par {nom_du_sorcier}
    def lancer_un_sort(self):
        print(f'Lancer un sort par {self.name}')

# Créer une instance de sorcier
voldemort = Wizard('voledmort', 'serpentard')

# Créer une instance de moldu
dursley = Moldu('dursley')

# Tenter de lancer un sort depuis l'instance du sorcier.
voldemort.lancer_un_sort()

# Tenter de lancer un sort depuis l'instance du moldu.
dursley.lancer_un_sort()

