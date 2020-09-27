import math , random

s = float(input('Enter a number with decimal: '))

print('Rounded up your number: ' , math.ceil(s))
print('Rounded down your number: ' , math.floor(s))

num = 4

print( num , 'Squared: ' , math.pow(num,2))
print( num , 'Squared Root: ' , math.sqrt(num))

nums = random.sample(range(1,49) , 6)

print('Your lotto luckey numbers are: ' , nums)

x = 2.634656
print(x)
print('%.2f'%x)