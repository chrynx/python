#-----------------functions-------------
def play_game():
 def print_board():
  for i in range(0,3):
   print board[i]
 board = []
 for i in range(3):
  board.append(['-','-','-'])
 print '--------------------'
 print 'Welcome to tic-tac-toe'
 print '--------------------'
 print
 p1 = raw_input('Please enter the first player\'s name -> ')
 p2 = raw_input('Please enter the second player\'s name -> ')
 print '--------------------'
 print 'Hello ' + p1 + ' and ' + p2 + ', and welcome to the game '
 turn = 0
 x_turn = True
 win_condition = False
 while win_condition == False:
  print_board()
#--------player 1 turn------------
  if x_turn == True:

   print 'it\'s ' + p1 + '\'s turn'
   choose_row = int(raw_input('choose a row (0-2) -> '))
   choose_col = int(raw_input('choose a col (0-2) -> '))
   row = board[choose_row]
   while row[choose_col] != '-':
    print 'That position has already been taken'
    choose_row = int(raw_input('choose a row (0-2) -> '))
    choose_col = int(raw_input('choose a col (0-2) -> '))
    row = board[choose_row]
   row[choose_col] = 'X'
   turn = turn + 1

#--------player 2 turn------------
  if x_turn == False:
   print 'it\'s ' + p2 + '\'s turn'
   choose_row = int(raw_input('choose a row (0-2) -> '))
   choose_col = int(raw_input('choose a col (0-2) -> '))
   row = board[choose_row]
   while row[choose_col] != '-':
    print 'That position has already been taken'
    choose_row = int(raw_input('choose a row (0-2) -> '))
    choose_col = int(raw_input('choose a row (0-2) -> '))
    row = board[choose_row]
   row[choose_col] = 'O'
   turn = turn + 1

  print '--------------------'
  for i in range(3):
   vert_x = ''
   diag_x = ''
   vert_o = ''
   diag_o = ''
   x_line = ['X','X','X']
   o_line = ['O','O','O']
   row = board[i]
   row_1 = board[0]
   row_2 = board[1]
   row_3 = board[2]
   if row_1[i] == 'X' and row_2[i] == 'X' and row_3[i] == 'X':
    vert_x = 'X'
   if row[i] == 'O' and row_2[i] == 'O' and row_3[i] == 'O':
    vert_o = 'O'
   if row_1[0] == 'X' and row_2[1] == 'X' and row_3[2] == 'X' or row_1[2] == 'X' and row_2[1] == 'X' and row_3[0] == 'X':
    diag_x = 'X'
   if row_1[0] == 'O' and row_2[1] == 'O' and row_3[2] == 'O' or row_1[2] == 'O' and row_2[1] == 'O' and row_3[0] == 'O':
    diag_o = 'O'
   if row == x_line or row == o_line or vert_x == 'X' or vert_o == 'O' or diag_x == 'X' or diag_o == 'O':
    print_board()
    if row == x_line or vert_x == 'X' or diag_x == 'X':
     print p1 + ' wins the game!'
    elif row == o_line or vert_o == 'O' or diag_o == 'O':
     print p2 + ' wins the game!'
    win_condition = True
   if turn == 9:
    print_board()
    print 'It is a draw! Nobody wins!'
    win_condition = True
   if x_turn == True:
    x_turn = False
   elif x_turn == False:
    x_turn = True
 print 'Thanks for playing the game'
 print 'Goodbye'
 exit()
#----------functions end----------------
play_game()
