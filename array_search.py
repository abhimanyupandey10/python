search = int(input('Which number do you want t search(0-9): '))

numbers = [1,9,3,6,8,4,7,5,2,0,7,2]

count = 0

found = False

for x in numbers:
    
    count = count + 1
    
    if x == search:
        found = True
        print(search , 'found on position' , count)

if found == False:
    print('number not found')