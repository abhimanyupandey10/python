# This program finds sum of even numbers of array using function

def findSumOfEvenNmbers (numbers):
    sum = 0
    for x in numbers:
        if x % 2 == 0:
            sum = sum + x

    return sum

####################### Main code starts #####################

numbers = [6,7,8,9,1,2,3,4,5,6]

sum = findSumOfEvenNmbers (numbers)
print (sum)