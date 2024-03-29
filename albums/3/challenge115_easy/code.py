'''
A "guess-that-number" game is exactly what it sounds like: a number is guessed
at random by the computer, and you must guess that number to win! The only
thing the computer tells you is if your guess is below or above the number.

Your goal is to write a program that, upon initialization, guesses a number
between 1 and 100 (inclusive), and asks you for your guess. If you type a
number, the program must either tell you if you won (you guessed the
computer's number), or if your guess was below the computer's number, or if
your guess was above the computer's number. If the user ever types "exit",
the program must terminate.

At run-time, expect the user to input a number from 1 to 100 (inclusive), or
the string "exit", and treat all other conditions as a wrong guess.
Output Description

The program must print whether or not your guess was correct, otherwise print
if your guess was below or above the computer's number.
Sample Inputs & Outputs

Let "C>" be the output from your applicatgion, and "U>" be what the user types:

C> Welcome to guess-that-numbers game! I have already picked a number in [1, 100].
Please make a guess. Type "exit" to quit.
U> 1
C> Wrong. That number is below my number.
U> 50
C> Wrong. That number is above my number.
...
U> 31
C> Correct! That is my number, you win! <Program terminates>

'''

import random

def report(comp, n):
    if n < comp:
        return 'Wrong! That number is below my number.'
    elif n > comp:
        return 'Wrong! That number is above my number.'
    else:
        return 'You win! This is my number!'

accum = 0
computer_guess = random.randrange(1, 101)

print('C> Welcome to guess-that-numbers game! I have already picked a number in [1, 100].\
    Please make a guess. Type "exit" to quit.')


while accum < 6:
    player = input('U>  ')
    try:
       player = int(player)
    except ValueError:
        if player == 'exit':
            exit()
        else:
            print('Not a valid entry, try again!')
            continue

    ans = report(computer_guess, player)
    print(ans)
    accum += 1

print('Timed out!')