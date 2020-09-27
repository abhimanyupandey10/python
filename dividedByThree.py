# This program finds the numbrs that can be divided by 3 using function and array

def findSumOfNumbersDividedByThree  (numbers):
    sum = 0
    for x in numbers:
        if x % 3 == 0:
            sum = sum + x

    return sum




numbers = [3,6,9,12,15,18]

findSum = findSumOfNumbersDividedByThree (numbers) 

print (findSum)