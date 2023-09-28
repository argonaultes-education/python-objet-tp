
try:
    f = open('test12.txt', 'r')
    print(f.read())
except:
    print('this file does not exist')