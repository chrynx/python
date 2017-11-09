print 'hello and welcome to tic-tac-toe'
#------------variables-------------
board = []
for i in range(3):
 board.append(['-','-','-'])
#----------------------------------
#-------------functions------------
def greeting(name):
 print 'thank you ' + name + ', welcome to the game '



def play_game(pl1,pl2):
 win_condition = False
 x_turn = True
 while win_condition == False:
  for i in range(0,3):
   print board[i]
  if x_turn == True:
   print 'it is ' + pl1 + '\'s turn '
  if x_turn == False:
   print 'it is ' + pl2 + '\'s turn '
  if x_turn == True:
   choose_row = 0
   choose_col = 0
   def position(choose_row, choose_col):
    choose_row = int(raw_input('choose a row'))
    choose_col = int(raw_input('choose a col'))
   position(choose_row, choose_col)
   row = board[choose_row]
   while row[choose_col] != '-':
    print 'choose a different position - this one\'s taken'
    position(choose_row, choose_col)
   row[choose_col] = 'X'
  if x_turn == False:
   choose_row = 0
   choose_col = 0
   def position(choose_row, choose_col):
    choose_row = int(raw_input('choose a row'))
    choose_col = int(raw_input('choose a col'))
   position(choose_row, choose_col)
   row = board[choose_row]
   while row[choose_col] != '-':
    print 'choose a different position - this one\'s taken'
    position(choose_row, choose_col)
   row[choose_col] = 'O'
  if x_turn == True:
   x_turn = False
  else:
   x_turn = True
#----------------------------------
pl1 = raw_input('please tell me, who is the first player? -> ')
greeting(pl1)
pl2 = raw_input('and the second player? -> ')
greeting(pl2)
print
print
print
play = raw_input('are you ready to play? (y/n)')
if play == 'y':
 print 'okay ' + pl1 + ' and ' + pl2 + ', let\'s play!!'
 play_game(pl1,pl2)
if play == 'n':
 for i in range(3):
  print
 print 'thank you for playing, see you again soon'
 exit
