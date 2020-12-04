from colorama import init, Fore
from termcolor import colored

class customBoard:

    #-----------------------------------------------------------#
    #                   INITIALIZATION                          #
    #-----------------------------------------------------------#
    def __init__(self):
        # Make board pieces "colorized"
        self.vb = self.yellow("|")
        self.s = self.yellow("\t  +---+---+---+")
        self.title = self.green("\t     columns")
        self.c = self.green("\t    1   2   3")
         
        #Initialize the board
        self.arrays = 3 
        self.board = [['*'] * 3 for i in range(self.arrays)]
        print(self.board)


    #-----------------------------------------------------------#
    #                           COLORS                          #
    #-----------------------------------------------------------#
    def red(self,v):
        return colored(v,"red", None, ['bold'])
    
    def blue(self,v):
        return colored(v,"blue", None, ['bold'])

    def yellow(self,v):
        return colored(v,"yellow", None, ['bold'])

    def green(self,v):
        return colored(v,"green", None, ['bold'])

    def magenta(self,v):
        return colored(v,"magenta", None, ['bold'])


    #-----------------------------------------------------------#
    #                       Track board moves                   #
    #-----------------------------------------------------------#
    def make_move(self, row, col, play):
        # update the array with the move/play
        self.board[row-1][col-1] = play


    #-----------------------------------------------------------#
    #                       Print Board                         #
    #-----------------------------------------------------------#
    def show_board(self):

        # print a small test board
        for array in range(self.arrays):
            for val in range(self.arrays):
                print(self.add_color(self.board[array][val]), end =" ")
            print()

        # print the colored board
        count =0
        rows = colored("rows","green", None, ['bold'])
        print(self.title)
        print(self.c)
        for row in self.board:
            count +=1
            countstr = self.green(str(count))
            if count == 2:
                print(self.s)
                print (rows+"\t" + countstr + " " + self.vb + " " + self.add_color(row[0]) + " " + self.vb + " " + self.add_color(row[1]) + " " + self.vb + " " + self.add_color(row[2]) + " " + self.vb)
            else:
                print(self.s)
                print ("\t" + countstr + " " + self.vb + " " + self.add_color(row[0]) + " " + self.vb + " " + self.add_color(row[1]) + " " + self.vb + " " + self.add_color(row[2]) + " " + self.vb)
        print(self.s)

        # print what is currently in the "board" array
        print(self.board)

    #-----------------------------------------------------------#
    #                       Check SCORE                         #
    #-----------------------------------------------------------#
    def check_score(self):
        if self.checkDiagonal():
            return True
        elif self.checkRows():
            return True
        elif self.checkColumns():
            return True
        else:
            print("okay")
            return False
            
    #                                       #
    # more functions for checking the score #
    #                                       #

    # check rows 
    def checkRows(self):
        print("check rows")
        for row in self.board:
            if row[1] != "*":
                if row[0] == row[1] == row[2]:
                    print("winner row")
                    return True
        return False
    # check columns
    def checkColumns(self):
        print("check columns")
        for col in range(3):
            if self.board[1][col] != "*":
                if self.board[0][col] == self.board[2][col] == self.board[1][col]:
                    print("winner column")
                    return True
        return False
    # check diagonals
    def checkDiagonal(self):
        print("check diagonals")
        if self.board[1][1] != "*":
            if self.board[1][1] == self.board[0][0] == self.board[2][2] or self.board[1][1] == self.board[0][2] == self.board[2][0]:
                print("winner diagonal")
                return True 
        return False


    #-----------------------------------------------------------#
    #                 Check slots available                     #
    #-----------------------------------------------------------#
    def check_moves_available(self):
        for array in range(self.arrays):
            for val in range(self.arrays):
                if self.board[array][val] == "*":
                    return True # yes moves are available
        return False # no moves are available

    def check_space_before_input(self,row,col):
        return self.board[row-1][col-1] == "*"


    #-----------------------------------------------------------#
    #          Add color based on the player "X" or "O"         #
    #-----------------------------------------------------------#
    def add_color(self, p):
        if p == "X":
            return self.red(p)
        elif p == "O":
            return self.blue(p)
        else:
            return p

    def add_winner_color_message(self,p,message):
        if p == "X":
            return self.red(message)
        else:
            return self.blue(message)