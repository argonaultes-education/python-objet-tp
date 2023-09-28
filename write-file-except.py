def ecrire_dans_fichier(file, content):
    with open(file, 'a') as f:
        f.write(content)

def ecrire_dans_fichier(file, content):
    try:
        f = open(file, 'a')
        f.write(content)
    except FileNotFoundError:
        print(f'Impossible d\'ouvrir le fichier {file}')
    except TypeError:
        print(f'Impossible d\'écrire dans {file}')
    else:
        print(f'{len(content)} caractères ont été ajoutés')
        f.close()

ecrire_dans_fichier('/tmp/tp/hello.txt', 12)