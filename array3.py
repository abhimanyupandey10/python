"""
1) ask the limit of array
2) enter numbers in array
3) check if any number in the array is odd
4) if true, turn that number to 0
"""
def get_limit():
    limit = int(input('Enter limit: '))
    return limit

def get_array(limit):
    array = [0]*limit

    for i in range(0,limit):
        array[i] = int(input('Enter number: '))

    return array

def update_array (array):
    for i in range(0,len(array)):
        if array[i] % 2 != 0:
            array[i] = 0

    return array

def main():
    limit = get_limit()
    array = get_array(limit)
    print(array)
    print()
    array = update_array(array)
    print(array)

main()    