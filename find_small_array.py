# This program finds smallest number in the array using function

def getArray():
    return [8,4,7,3,5]
    
def findSmallest(ar):
    small = ar[0]

    for x in ar:
        if x < small:
            small = x

    return small
                        

def printSmallest(smallest):
    print('Smallest number in the array is: ', smallest)

# Main code 

ar = getArray()
smallest = findSmallest(ar)
printSmallest(smallest)