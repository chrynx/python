board = [
['-','-','-'],
['-','-','-'],
['-','-','-']
]

for i in range(3):
  print board[i]

objects = 1

while objects != 9:
  choose_row = int(raw_input('please choose the row ( 0 - 2 )'))
  choose_col = int(raw_input('please choose the col ( 0 - 2 )'))

  row = board[choose_row]
  row[choose_col] = 'X'

  for i in range(3):
    print board[i]
  
  objects += 1
