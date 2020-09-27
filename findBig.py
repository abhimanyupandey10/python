# how to find big in three numbers?
def findBig (a,b): 
    if a > b:
        return a
    else:
        return b

        
a = 56
b = 4
c = 58

big = findBig (a,b)
big = findBig (big,c)

print (big) 