import random 

Board_height = 3
Board_width = 3 


# Create new board of width 3 and height 3 
def new_board():
    board = []
    for x in range(Board_width):
        column = []
        for y in range(Board_height):
            column.append(None)
        board.append(column)
    return board


# Display the board 
def render(board):

    row_num = 0
    print("   0 1 2 ")
    print("  ------")
    for row in board:
        output_row = ""
        for square in row:
            if square is None:
                output_row += " "
            else:
                output_row += square
        print("%d|%s|" % (row_num, ' '.join(output_row)))
        row_num += 1
    print("  ------")


board = new_board()
board[2][1] = "x"
board[1][1] = "o"
render(board)
