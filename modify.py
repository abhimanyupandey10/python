string = str(input('Enter a word: '))

print ('\nCapitalized:\t' , string.capitalize())
print ('\nTitled:\t\t' , string.title())
print ('\nCentered:\t' , string.center(30 , '*'))

print ('\nUpercase:\t' , string.upper())
print ('\nJoined:\t\t' , string.join ('**'))

print ('\nJustified:\t' , string.rjust(30, '*'))

print ('\nReplaced:\t' , string.replace('i' , '*'))           