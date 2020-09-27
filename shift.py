def get_limit():
    limit = int(input('Enter limit: '))
    return limit

def get_array(limit):
    arr = [0]*limit

    for i in range(0,limit):
        arr[i] = int(input('Enter number: '))

    return arr

def direction_of_shifting():
    direction = str(input('Enter direction: '))
    return direction
   

def get_shifting_limit():
    shift = int(input('How many shifts?: ')) 
    return shift  


def shifting_array_left(arr,shift):
    temp = arr[0]
    size = len(arr)
   
    for j in range(0,size - 1):
        arr[j] = arr[j + 1]
            
    arr[size-1] = temp

    return arr
    


def shifting_array_right(arr,shift):
    size = len(arr)
    temp = arr[size - 1]

    for i in range(0,size - 1):
        arr[size - i - 1] = arr[size - i - 2]

    arr[0] = temp

    return arr



def main():
    limit = get_limit()
    arr = get_array(limit)
    direction = direction_of_shifting()
    shift = get_shifting_limit()
    
    print (arr)
   
    if direction == 'right':
        for _ in range(1,shift+1): 
            arr = shifting_array_right(arr,shift)
    elif direction == 'left':
        for _ in range(1,shift+1):
            arr = shifting_array_left(arr,shift)
    else:
        print('no direction like that')
        exit(0)
    
    print(arr)


main()