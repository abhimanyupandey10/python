a = input('Enter A Number:')
b = input('Now Enter Another Number:')

sum = a + b
print ( '\nData type sum :' , sum , type(sum))

sum = int(a) + int(b)
print ( 'Data type sum :' , sum , type(sum)) 

sum = float(sum) 
print ( '\nData type sum :' , sum , type(sum))

sum = chr(int(sum))
print ( 'Data type sum :' , sum , type(sum))    