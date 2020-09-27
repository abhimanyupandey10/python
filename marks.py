marks = int(input('Enter marks:'))
if marks > 100:
    print ('error, Invalid marks!')
elif marks == 100:
    print('congracts!, you gought full marks 1st grade')
elif marks == 80:
    print('well try but you gought 2nd grade') 
elif marks == 60:
    print('soory to say but you gought 3rd grade')
elif marks < 50:
    print('fail')