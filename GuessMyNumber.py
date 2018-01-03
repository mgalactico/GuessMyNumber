# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 (inclusive)
# and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess
# too high or too low? Using bisection search, the computer will guess the user's secret number!


def verify_response():
    user_response = input(
        'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is '
        'too low. Enter \'c\' to indicate I guessed correctly.')
    while user_response not in acceptedResponses:
        print('Sorry, I did not understand your input.')
        print('Is your secret number', guess, '?')
        user_response = input(
            'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess '
            'is too low. Enter \'c\' to indicate I guessed correctly.')
    return user_response


acceptedResponses = ['h', 'l', 'c']
start = 0
middle = 50
end = 100
print('Please think of a number between 0 and 100!')
print('Is your secret number', middle, '?')

response = verify_response()

while response != 'c':
    if response == 'l':
        guess = int((middle + end) / 2)
        start = middle
        middle = int((start + end) / 2)
        print('Is your secret number', guess, '?')

        response = verify_response()

    elif response == 'h':
        guess = int((start + middle) / 2)
        end = middle
        middle = int((start + end) / 2)
        print('Is your secret number', guess, '?')

        response = verify_response()

print('Game over. Your secret number was:', guess)
