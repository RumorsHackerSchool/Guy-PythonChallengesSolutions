'''
ESTIMATED TIME TO COMPLETE: 15 minutes

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

'''

print("Please think of a number between 0 and 100!")
guess = 50
print("Is your secret number 50?")
ans = str(input(
    "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
while ans != 'c':
    if ans == 'h':
        guess = guess/2
        print("Is your secret number" + str(guess) + "?")
        ans = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))

    elif ans == 'l':


