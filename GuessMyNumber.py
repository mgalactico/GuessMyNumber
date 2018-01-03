# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 (inclusive)
# and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess
# too high or too low? Using bisection search, the computer will guess the user's secret number!

acceptedResponses = ['h', 'l', 'c']
start = 0
answer = middle = 50
end = 100
print('Please think of a number between 0 and 100!')
print('Is your secret number', middle, '?')
response = input(
    'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
while response not in acceptedResponses:
    print('Sorry, I did not understand your input.')
    print('Is your secret number', answer, '?')
    response = input(
        'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
while response != 'c':
    if response == 'l':
        guess = int((middle + end) / 2)
        start = middle
        middle = int((start + end) / 2)
        answer = guess
        print('Is your secret number', answer, '?')
        response = input(
            'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
        while response not in acceptedResponses:
            print('Sorry, I did not understand your input.')
            print('Is your secret number', answer, '?')
            response = input(
                'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    elif response == 'h':
        guess = int((start + middle) / 2)
        end = middle
        middle = int((start + end) / 2)
        answer = guess
        print('Is your secret number', answer, '?')
        response = input(
            'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
        while response not in acceptedResponses:
            print('Sorry, I did not understand your input.')
            print('Is your secret number', answer, '?')
            response = input(
                'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
print('Game over. Your secret number was:', answer)
