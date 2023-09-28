file_ages = open('ages.txt', 'r')
for age in file_ages:
    try:
        if int(age) > 18:
            print('Age {age} est majeur'.format(age = age[:-1]))
        else:
            print('Age {age} n\'est pas majeur'.format(age = age[:-1]))
    except:
        print(f'Age {age} non valide')
file_ages.close()

