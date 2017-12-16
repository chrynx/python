gameboard = []
for i in range(0,8):
    board_row = []
    for j in range(0,8):
        board_row.append('-')
    gameboard.append(board_row)
def print_board():
    for i in range(0,8):
        print gameboard[i]

for i in range(0,8):
    white_pawn = gameboard[1]
    black_pawn = gameboard[6]
    white_pawn[i] = 'P'
    black_pawn[i] = 'P'


print_board()
