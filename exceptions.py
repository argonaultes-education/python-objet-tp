# fonction appelée ecrire_dans_fichier qui prend 2 paramètres
def ecrire_dans_fichier(filename, content):
    try:
        # ouvrir un fichier en ajout
        file = open(filename, 'a')
        # ajouter le contenu de content dans le fichier
        file.write(content)
        # afficher la taille de la chaine de caractère qui a été ajoutée
        print('Nb de caractères ajoutés : {0}'.format(len(content)))
        # fermer le fichier
        file.close()
    except FileNotFoundError:
        print(f'Le fichier \'{filename}\' est introuvable.')
    except TypeError:
        print(f'Impossible d\'écrire dans le fichier \'{filename}\'')
ecrire_dans_fichier('not_exist/test.txt', 'hello')
ecrire_dans_fichier('test.txt', 12)