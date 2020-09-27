"""
1
1 2
1 2 3
1 2 3 4

"""

limit = int(input('Enter a limit'))
for i in range (1 , limit + 1):
    for j in range (1 , i + 1):
        print(j,end = ' ')
        
    print()

for i in range(1, limit + 1):
    for j in range(1, limit + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
