# CODE of find big

def find_big(a, b):
    if a > b:
        return (a)
    else:
        return (b)


# CODE of number square

def find_square(a):
    return a*a


# CODE of number cube
def find_cube(b):
    return b*b*b


# CODE of finding big in array

def find_big_in_array(numbers):
    big = numbers[0]

    for x in numbers:
        if x < big:
            big = x

    return big


# CODE to find sum of even numbers

def even_array_sum(numbers):
    sum = 0

    for x in numbers:
        if x % 2 == 0:
            sum = sum + x

    return sum


# Code to find biggest in list

def find_big_in_list (numbers):
    big = numbers[0]

    for x in numbers:
        if x > big:
            big = x

    return big