class game:
    board = [['','',''],['','',''],['','','']]

#player is identified by a character ('X' or 'O')
#check if player has won
    def win(self, player):
        if(self.board[0]== [player,player,player]):
           self.board = [['','',''],['','',''],['','','']]
           return True
        if(self.board[1]== [player,player,player]):
           self.board = [['','',''],['','',''],['','','']]
           return True
        if(self.board[2]== [player,player,player]):
           self.board = [['','',''],['','',''],['','','']]
           return True
        if(self.board[0][0]== player and self.board[1][0]== player and self.board[2][0]== player):
           self.board = [['','',''],['','',''],['','','']]
           return True
        if(self.board[0][1]== player and self.board[1][1]== player and self.board[2][1]== player):
           self.board = [['','',''],['','',''],['','','']]
           return True
        if(self.board[0][2]== player and self.board[1][2]== player and self.board[2][2]== player):
           self.board = [['','',''],['','',''],['','','']]
           return True
        if(self.board[0][0]== player and self.board[1][1]== player and self.board[2][2]== player):
           self.board = [['','',''],['','',''],['','','']]
           return True
        if(self.board[0][2]== player and self.board[1][1]== player and self.board[2][0]== player):
           self.board = [['','',''],['','',''],['','','']]
           return True
        return False

    def reset():
        board = [['','',''],['','',''],['','','']]

#player moves, returns true if they win, check if cell is already taken
    def move(self,player,cell):
        try:
            if(not self.board[(cell//3)%3][cell%3]==''):
                return "bad"
            else:
                self.board[(cell//3)%3][cell%3] = player
            if(self.win(player)):
                return "win"
            return "good"
        except:
            return "bad"

    def gameLoop():
        x =game()

        print (x.board[0])
        print (x.board[1])
        print (x.board[2])



        player = 'X'
        while(1):
            inp1, inp2 = input('Enter coordonates:').split()
            inp1 = int(inp1)
            inp2 = int(inp2)
            if(x.move(player,inp1-1,inp2-1)):
                print ("player "+player+" wins!!")
            if(player=='X'):
                player = 'O'

            elif(player=='O'):
                player = 'X'

            print (x.board[0])
            print (x.board[1])
            print (x.board[2])
