try:
    x = int(input('ENTER NUMBER:'))
except ValueError as err:
    print('!Invalid!, only intiger to be entered')
    exit ()

print(x*x)