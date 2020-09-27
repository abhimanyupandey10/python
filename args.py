def echo(user,lang,sys):
    print('User: ' , user, 'Language: ' , lang , 'Platform: ' , sys)

echo('Abhimnyu' , 'Python' , 'Windows 10')

echo(lang = 'Python' , sys = 'Windows 10' , user = 'Ronny')

def mirror (user = 'Delkish' , lang = 'Python'):
    print('\nUser:' , user , 'Language: ' , lang)

mirror()
mirror( lang = 'Java')
mirror(user = 'Tonny')
mirror('Sussan' , 'C++')