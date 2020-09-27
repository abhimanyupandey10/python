#This program prints the second biggest number in the array

def find_big (numbers):
    
    big = numbers[0]

    for x in numbers:
        if x > big:
            big = x

    return big
#finds second big#
def find_second_big (numbers , big):
    
    secondBig = numbers[0]

    for x in numbers:
        print(number, ' , ' , big , ' , ' , secondBig)
        if secondBig < big and secondBig != big:
            secondBig = num

    return big
array = [35,467,578,245,5678,356]

big = find_big(array)

print('The biggest number in the array is: ' , big)