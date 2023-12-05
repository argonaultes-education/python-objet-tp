# Créer une classe Moldu
class Moldu:

    # La classe Moldu a un attribut d'instance initialisé à la construction : nom
    def __init__(self, name):
        self.name = name

# Créer une classe Sorcier
# Sorcier hérite de Moldu
class Sorcier(Moldu):

    # La classe Sorcier a un attribut d'instance initialisé à la construction : house
    # Ajout du paramètre nom pour appeler le constructeur parent
    def __init__(self, house, name):
        # initialise l'état de la classe parent, c'est à dire Moldu
        super().__init__(name)
        self.house = house
    
    # Ajouter la méthode lancer un sort
    def lancer_un_sort(self):
        print(f'Lancer un sort par {self.name}')

if __name__ == '__main__':
    vernon = Moldu('vernon')
    hermione = Sorcier('poufsouffle', 'hermione')
    hermione.lancer_un_sort()

    harry = Sorcier('poufsouffle', 'harry')
    harry.lancer_un_sort()
    print(f'{hermione.name} is a magician')