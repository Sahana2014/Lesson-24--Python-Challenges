import random
import time

number = random.randint(1, 100)

def intro():
    print("May I ask your name?")
    global name
    name = input()
    print(name + ", We are going to play a number guessing game. I am thinking of a number between 1 and 100.")
    
    if(number % 2 == 0):
        x = "even"
    else:
        x = "odd"
    print("\n This is a {} number ".format(x))
    time.sleep(.5)
    print("Go ahead. Guess!")
    
def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Guess: ")
        
        try:
            guess = int(enter)
            if guess<=100 and guess>=1:
                guessesTaken =guessesTaken + 1
                
                if guessesTaken < 6:
                    if guess < number:
                        print("Your guess is too low.")
                    if guess > number:
                        print("Your guess is too high.")
                    if guess != number:
                        time.sleep(.5)
                        print("Try again")
                        
                    if guess == number:
                        break
                    
            if guess>100 or guess<1:
                print("Silly goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")
        except: 
            print("I don't think that "+ enter + " is a number. Sorry")  
    
    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good job {}! You guessed my number in {} guesses!".format(name, guessesTaken))    
    if guess != number:
        print("Nope. The number I was thinking of was " + str(number))   
        
playagain = 'yes'
while playagain == 'yes' or playagain == 'y' or playagain == 'Yes' or playagain == 'Y':
    intro()
    pick()
    print("Would you like to play again?")
    playagain = input()      
        