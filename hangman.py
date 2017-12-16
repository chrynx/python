print('##########################################')
print()
print('############ WELCOME TO HANGMAN ##########')
print()
print('##########################################')
import random
def game():
    words = ['president', 'natoora', 'apple', 'pears', 'orangers', 'cellphone']
    current_word = words[random.randint(0,(len(words) -1))]
    def print_word():
        print('*'*len(current_word))
    print('Hello and welcome to Hangman')
    print('First of all, what is your name?')
    player_name = raw_input()
    print('Thank you ' + player_name)
    print
    print
    print('Now, this is the word you have to guess')
    print_word()
    print('Choose a letter')
    guess_letter = raw_input()
game()
print('Thanks for playing hangman today')
print('Have a good day')
print('Goodbye')
