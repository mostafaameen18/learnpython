import os
class tictactoe:

    def __init__(self, pl1name, pl2name):
        self.pl1name = pl1name
        self.pl2name = pl2name

#function on starting game

    def startgame(self):
        self.ticlist = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = 0
        print('welcome to TicTacToe \nProgrammed by MOSTAFA AMEEN')
        self.showres()



#WHAT HAPPENS WHEN SOME PLAYER WINS
    def playerwins(self):
        print("#################################################################################\n")
        print("#################################################################################")
        if self.player == 1:
            print("{} wins #############".format(self.pl1name))
        else:
            print("{} wins #############".format(self.pl2name))
        print("#################################################################################\n")
        print("#################################################################################")
        self.again = input('do you want to play again (y/n): ')
        if self.again == 'n':
            return 0
        else:
            self.startgame()


#WHAT HAPPENS WHEN GAME ENDS DRAW
    def endgame(self):
        print("#################################################################################\n")
        print("#################################################################################")
        print("Game finished >>> Nobody wins !!")
        print("#################################################################################\n")
        print("#################################################################################")
        self.again = input('do you want to play again (y/n): ')
        if self.again == 'n':
            print('Thanks for playing')
        else:
            self.startgame()

#CHECKING RESULT TO SEE IF THERE IS A WINNER OR THE GAME ENDED DRAW
    def checkresult(self):
        for i in range(3):
            if self.ticlist[i][0] == self.ticlist[i][1] == self.ticlist[i][2] or self.ticlist[0][i] == self.ticlist[1][i] == self.ticlist[2][i] or self.ticlist[0][0] == self.ticlist[1][1] == self.ticlist[2][2] or self.ticlist[0][2] == self.ticlist[1][1] == self.ticlist[2][0]:
                self.playerwins()

        if self.valid == []:
            self.endgame()
        else:
            self.turn += 1
            self.play()



#FUNCTION FOR TAKING THE INPUT OF PLAYING POSITION FORM PLAYER
    def play(self):


        if self.turn % 2 != 0:
            self.player = 1
            self.pl = self.pl1name
        else:
            self.player = 2
            self.pl = self.pl2name

        print('player {} turn'.format(self.pl))

        if self.player == 1:
            self.char = 'O'
        else:
            self.char = 'X'

        try:
            self.sign = int(input("enter the numer of the place you want to play in: "))
        except:
            print('wrong entery !!')
            return self.play()

        if self.sign in self.valid:
            self.putchar()
        else:
            print('wrong entery !!')
            self.play()



#FUNCTION FOR PUTTING THE CHAR IN ITS POSITION IN THE TICTACTOE MATRIX
    def putchar(self):
        if self.sign == 1 or self.sign == 2 or self.sign == 3:
            self.row = 0
        elif self.sign == 4 or self.sign == 5 or self.sign == 6:
            self.row = 1
        elif self.sign == 7 or self.sign == 8 or self.sign == 9:
            self.row = 2

        if self.sign == 1 or self.sign == 4 or self.sign == 7:
            self.col = 0
        elif self.sign == 2 or self.sign == 5 or self.sign == 8:
            self.col = 1
        elif self.sign == 3 or self.sign == 6 or self.sign == 9:
            self.col = 2


        self.ticlist[self.row][self.col] = self.char
        self.valid.remove(self.sign)
        self.showres()


#FUNCTION OF SHOWING THE RESULT
    def showres(self):
        os.system("clear")
        for sublist in self.ticlist:
            print("|", end=" ")
            for i in sublist:
                print(i, end=" | ")
            print("\n")

        self.checkresult()

pl1name = input('enter first player name: ')
pl2name = input ('enter second player name: ')
game = tictactoe(pl1name, pl2name)
game.startgame()
