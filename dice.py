print 'Hello World'

from random import randint

dice = randint(1,6)
choice = int(raw_input('Have a guess what the result of the roll is! (please input a number from 1 - 6) '))
print 'The die shows a ' + str(dice)
print 'The player chooses ' + str(choice)
