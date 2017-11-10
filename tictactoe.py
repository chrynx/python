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
   position = False
   while position == False:
     try:
      choose_row = int(raw_input('choose a row (0-2) -> '))
      while choose_row > 2 or choose_row < 0:
       choose_row = int(raw_input('choose a row (0-2) -> '))
      choose_col = int(raw_input('choose a col (0-2) -> '))
      while choose_col > 2 or choose_col < 0:
       choose_col = int(raw_input('choose a col(0-2) -> '))
      position = True
     except ValueError:
      print 'please only input numbers'
   row = board[choose_row]
   row[choose_col] = 'X'
   if row[0] == 'X' and row[1] == 'X' and row[2] == 'X':
    print pl1 + ' has won!'
    print 'goodbye'
    quit()
  if x_turn == False:
   print 'it is ' + pl2 + '\'s turn '
   try:
    choose_row = int(raw_input('choose a row (0-2) -> '))
    choose_col = int(raw_input('choose a col (0-2) -> '))
   except ValueError:
    print 'enter the right value'
   row = board[choose_row]
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
