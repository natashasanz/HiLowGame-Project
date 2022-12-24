#Natasha Sanchez 
#11/07/22
#Sanchez-HiLowGame
#This application will allow you to play hi/low game! 
#Place your maximum value, and guess a number within the bounds until you get the correct number.
#You can pick the highest number possible while the lowest number is alwasy one.

import random

repeat_game = 'Y'
while repeat_game == 'Y':

    maximun_number = int (input ('What should the maximun number for this game be? '))
    num = random.randint(1,maximun_number)
    guess = int(input('Guess my number: '))

    while guess != num:
        if guess > num:
            print ('Your guess is too high')
            guess = int(input('Guess my number: '))
        elif guess < num:
            print ('Your guess is too low')
            guess = int(input('Guess my number: '))
    print ('You guessed my number!')
    repeat_game = input ('Do you wish to play again? (Y/N): ').upper()
    
print('Thank you for playing!')




