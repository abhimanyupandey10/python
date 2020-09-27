# how to find biggest number using array?
def findBig (numbers):
    '''finds big in array '''
    big = numbers [0] 

    for x in numbers:
        if x > big: 
            big = x

    return big


ar = [34,78,34,89,23,679,468,578,568,458,468,46]

big = findBig(ar)

print(big)

print(findBig.__doc__)