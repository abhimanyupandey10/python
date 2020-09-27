print(' ')
text = str(input('Enter a text: '))
print(' ')
search = str(input('Enter seaech word: ')) 

# finding word in text

found = (search in text)
if found:
    print('\nYes the word is there')
else:
    print('No word found')
print(' ')

