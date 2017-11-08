#print 'Hello World'

from random import randint

dice = randint(1,6)
userChoice = False

while userChoice == False:
  try:
    choice = int(raw_input('Have a guess what the result of the roll is! (please input a number from 1 - 6) '))
    if choice >= 1 and choice <= 6:
      userChoice = True
    else:
      print('Please enter a valid number')
  except ValueError:
    print('Please enter a valid number')
print 'The die shows a ' + str(dice)
print 'The player chooses ' + str(choice)
if dice == choice:
  print 'Well done! You have guessed the roll correctly!'
else:
  print 'Better luck next time!'
