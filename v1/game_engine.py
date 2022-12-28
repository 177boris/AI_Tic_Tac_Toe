### Unfinished ### 


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
    
    print(" -------")
    for row in rows:
        output_row = ""
        for square in row:
            if square is None:
                output_row += "_"
            else:
                output_row += square
        print("%d|%s|" % (row_num, ' '.join(output_row)))
        row_num += 1
    print(" -------")
    print("  0 1 2 ")


# Get player's move 
def get_move():

    x_coord  = int(input("Enter the x coordinate:   "))    # get X-coordinate 
    y_coord  = int(input("Enter the y coordinate:   "))    # get Y-coordinate 

    valid_move = x_coord >= 0 and x_coord <= 2 and y_coord >= 0 and y_coord <= 2   # check if move is valid

    while(not valid_move):
        print("Please enter a valid move")
        return get_move()

    move_coord = (x_coord, y_coord)      # convert to tuple

    make_move(board, move_coord, "x")

    return move_coord                              


# Check if board is full 
def isBoardFull(board):
    for col in board:
        for square in col:
            if square is None:  # if there is an empty square, return false 
                return False

    return True


def make_move(board, coordinates, player):

    board[coordinates[0]][coordinates[1]] = player

    return board



board = new_board() # Create new board 

# Test render function 
#board[0][2] = "x"
#board[1][1] = "o"
#board[0][1] = "x"
#render(board)

move_coords = get_move() 
render(board)