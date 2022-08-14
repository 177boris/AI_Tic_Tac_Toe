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

    rows = []
    for y in range(0, Board_height):
        row = []
        for x in range(0, Board_width):
            row.append(board[x][y])
        rows.append(row)

    row_num = 0
    
    print("  ------")
    for row in rows:
        output_row = ""
        for square in row:
            if square is None:
                output_row += "_"
            else:
                output_row += square
        print("%d|%s|" % (row_num, ' '.join(output_row)))
        row_num += 1
    print("  ------")
    print("  0 1 2 ")


# Get player's move 
def get_move():

    # get X-coordinate 
    # get Y-coordinate 
    pass 


board = new_board() # Create new board 

# Test render function 
board[0][2] = "x"
board[1][1] = "o"
board[0][1] = "x"
render(board)
