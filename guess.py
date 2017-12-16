import random
a = random.randint(1,100)

print('####################')
print('# GUESS THE NUMBER #')
print('####################')

print('What is your name?')
name = raw_input()
print('Thank you for playing today ' + name)
print('Would you like to guess the number?')
print('Please choose a number between 1 and 100')
guessed = False
while guessed == False:
    guess = input()
    if guess < a:
        print('Your guess is lower than the number')
    if guess > a:
        print('Your guess is higher than the number')
    if guess == a:
        global guessed
        guessed = True
print('You have guessed the number!')
print('Thank you for playing')
print('Goodbye')
