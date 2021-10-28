#This is a guess game..
import random
print('Hello,dude what is your name?')
name=input()
print('Well,'+name+',I am thiking no. between 1 to 20')
secretNumber=random.randint(1, 20)

for guessTaken in range(1, 7):

    while True:
        try:
            print('Take a guess')
            guess=int(input())
            break
        
        except ValueError:
                print('this is not number dude')
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too High')
    else:
        break  #This condition is for correct guess.
if guess == secretNumber:
    print('Good job,'+name+'! You guessed my number '+str(guessTaken)+' guess')
else:
    print('Nope! The number i thinking was of '+str(secretNumber))
