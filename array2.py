"""
1) ask name
2) show wepons
3) ask which wepon to use 
4) minus the hp of the player
"""
import random
alex = 100
gama = 100

wepon = ['Knife' , 'sword' , 'hammer' , 'punch']

a = str(input('Select name(alex/gama): '))
if a == 'alex':
    print('OK, your opponent is gama')
    player1 = 'gama'
    player2 = 'alex'
    opponent = gama
    me = alex
elif a == 'gama':
    print('OK, your opponent is alex')
    player1 = 'alex'
    player2 = 'gama'
    opponent = alex
    me = gama
else:
    print('NO name')
    exit(0)
knife_damage = 20
sword_damage = 60
hammer_damage = 40
punch_damage = 10
print( )
print('your wepons are sword , knife , hammer , punch')
print( )
b = str(input('which wepon you want to use on your opponent: '))
if b == 'knife':
    damage = opponent - knife_damage
    print('your opponent has ' , damage , 'hp')

elif b == 'sword':
    damage = opponent - sword_damage
    print('your opponent has ' , damage, 'hp')
elif b == 'punch':
    damage = opponent - punch_damage
    print('your opponent has ' , damage, 'hp')
elif b == 'hammer':
    damage = opponent - hammer_damage
    print('your opponent has ' ,damage, 'hp')
else:
    print('no wepon like that')
    exit(0)
number = random.randint(10,60) 
hp = me-number
print('he damaged you' , number , 'and now your hp is'  , hp)
print( )
if number > damage:
    print(a , 'won')
elif number < damage:
    print(a , 'won')
else:
    print('tie')
    