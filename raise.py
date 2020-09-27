try:
    x = int(input('ENTER NUMBER:'))
except ValueError as err:
    print('!Invalid!, only integer to be entered')
    exit ()

print("Square of ", x, "is", x*x)