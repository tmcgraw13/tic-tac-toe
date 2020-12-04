from board import customBoard

def userInput(p):
    space = True
    while(space):
        row = int(input("Input a row 1 2 or 3: "))
        column = int(input("Input a column  1 2 or 3: "))
        if board.check_space_before_input(row,column):
            board.make_move(row,column,p)
            space = False
        else:
            print(board.magenta("try again"))

#Start

# Initialize board
board = customBoard()

# Show board
board.show_board()

moves = True
p = "X"

while moves == True:
    print(board.add_color(p) + " your move")
    userInput(p)
    board.show_board()
    
    if board.check_score():
        print(board.add_winner_color_message(p,p + " is the winner"))
        moves = False
        
    if not board.check_moves_available() and moves!=False:
        print (board.magenta("It's a tie!"))
        moves = False
     

    if p == "X":
        p = "O"
    else:
        p = "X"

print("Thank you for playing my game!!!")