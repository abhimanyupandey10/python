import random

print("Number guessing game") 

number = random.randint(1, 100) 
  
chances = 0
  
print("Guess a number (between 1 and 100): ")  

while chances < 10: 
    guess = int(input()) 
      
    if guess == number: 
        print("Congratulation YOU WON!!!, you took" , chances , "chance to get the corect answer which is" , number) 
        break

    elif guess < number: 
        print("Your guess was too low: Guess a number higher than", guess) 

    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
          
 
    chances += 1
          

if not chances < 20: 
    print("YOU LOSE!!! The number is not coreect 12 times")
