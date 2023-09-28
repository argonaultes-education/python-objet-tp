def get_items_from_file(file):
    # ouvrir le fichier user.txt en lecture
    stream_file = open(file, 'r')
    # lire tout le fichier
    items_str = stream_file.read()
    # stocker les lignes dans une liste
    items = items_str.split('\n')
    return items

# ouvrir le fichier pass.txt en lecture
# lire tout le fichier
# stocker les lignes dans une liste

users = get_items_from_file('user.txt')
passwords = get_items_from_file('pass.txt')

# pour chaque élément de la liste utilisateur
#  associer chacun des éléments de la liste password
for user in users:
    for password in passwords:
        print(f'{user},{password}')

# mysql,12345
# mysql,qwerty
# mysql,webadmin
# mysql,webmaster

# Option2

if __name__ == '__main__':

    with open('user.txt', 'r') as user_file:
        with open('pass.txt', 'r') as pass_file:
            for user in user_file:
                print(user.strip())
                for password in pass_file:
                    print(f'{user.strip()},{password.strip()}')
                pass_file.seek(0)
