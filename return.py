num = input('Enter integer: ')

def square(num):

    if not num.isdigit():
        return 'Invalid Entery'

    num = int(num)     
    return num * num  

print( num , 'Squared is: ' , square(num))