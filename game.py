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
           return true
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

#player moves, returns true if they win
    def move(self,player,cell):
        try:
            if(cell==0):
                self.board[0][0] = player
            elif(cell==1):
                self.board[0][1] = player
            elif(cell==2):
                self.board[0][2] = player
            elif(cell==3):
                self.board[1][0] = player
            elif(cell==4):
                self.board[1][1] = player
            elif(cell==5):
                self.board[1][2] = player
            elif(cell==6):
                self.board[2][0] = player
            elif(cell==7):
                self.board[2][1] = player
            elif(cell==8):
                self.board[2][2] = player
            if(self.win(player)):
                return True
            return False
        except:
            return False

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
                print ("player "+player+" wins!!!!!!!! ;:^)")
            if(player=='X'):
                player = 'O'

            elif(player=='O'):
                player = 'X'

            print (x.board[0])
            print (x.board[1])
            print (x.board[2])
