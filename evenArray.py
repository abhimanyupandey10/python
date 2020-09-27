# This progarm finds sum of even numbers using array

numbers = [3347,467,589,5678,679,5789,6675,5779,257,678899,4678]
for x in numbers:
    if x%2 == 0:
        print (x)  


sum = 0
for x in numbers:
    sum = x + sum

print (sum)    