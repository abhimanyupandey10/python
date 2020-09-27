""""
WHAT TO DO: To arrange in desending order, the number which is greater should be on the first

|1,5|,3,8,4,9,2,6,7
5|,1,3|,8,4,9,2,6,7
5,3,|1,8|,4,9,2,6,7
5,3,8,|1,4|,9,2,6,7
5,3,8,4,|1,9|,2,6,7
5,3,8,4,9,|1,2,|6,7
5,3,8,4,9,2,|1,6|,7
5,3,8,4,9,2,6,|1,7|
5,3,8,4,9,2,6,7,1
but we need to bring: 9,8,7,6,5,4,3,2,1
"""

ar = [1,2,3,4,5,6,7,8,9]

print('Orignal numbers: ' , ar)

for i in range(1, len(ar)):
    for j in range(1, len(ar)):
        if ar[j] > ar[j-1]:
            temp = ar[j]
            ar[j] = ar[j-1]
            ar[j-1] = temp

numbers = ar
print('\nArranged numberes: ' , numbers)