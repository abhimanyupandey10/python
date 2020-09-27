s = 'Röd'
print('\nRed string:' , s)
print('Type:' , type(s) , '\tLeangth:' , len(s))

s = s.encode('utf-8')
print('\nEncode strings:' , s)
print('Type:' , type(s) , '\tLeangth:' , len(s))

s = s.decode('utf-8')
print('\ndecode strings:' , s)
print('Type:' , type(s) , '\tLeangth:' , len(s))