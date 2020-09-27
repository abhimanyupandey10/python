
luckey_number = str(input('What is your favourite, odd or even? : '))

if luckey_number == 'odd' or 'even':
    print('Cool')
else:
    print ('Sorry')
    exit(0)

number = int(input('which is your favourite number(if yoy have selected even then write a even number and for odd the same) : '))

print('great')

DM = str(input('What do you like ? multiplication or division: ' ))

if DM == 'multiplication':
    print(number * 2)
    

if DM == 'division':
    print(number % 2)