"""
STEPS:
step 1) creat a array of numbers by taking input from the user
step 2) count the number of even and odd numbers in the array
"""

def get_limit():
    limit = int(input('Enter limit: '))
    return limit

def get_array(limit):
    array = [0]*limit

    for i in range(0,limit):
        array[i] = int(input('Enter number: '))

    return array
    

def get_odd_sum(array): 
    sum = 0

    for i in range(0,len(array)):
        if array[i] % 2 != 0:
            sum = sum + array[i]

    return sum


def get_even_sum(array): 
    sum = 0

    for i in range(0,len(array)):
        if array[i] % 2 == 0:
            sum = sum + array[i]

    return sum



def main():
    limit = get_limit()
    array = get_array(limit)
    print(array)
    even_sum = get_even_sum(array)
    odd_sum = get_odd_sum(array)
    print('sum of all odd numbers is: '  , odd_sum)
    print('sum of all even numbers is: '  , even_sum)

main()