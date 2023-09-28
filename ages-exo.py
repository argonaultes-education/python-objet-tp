# ouvrir un fichier
with open('ages.txt', 'r') as file:
# parcourir le fichier ligne à ligne
    for age_str in file:
        try:
# pour chaque ligne, transformer en entier
            age = int(age_str)
    # tester si cet entier est plus grand que 18
            if age >= 18:
    # si plus grand que 18, afficher majeur
                print('age {0} majeur'.format(age))
    # sinon afficher mineur
            else:
#                print('age {0} mineur'.format(age))
                print(f'age {age} mineur')
        except:
            pass