class game:

    boards = []
    bigBoard =  [['','',''],['','',''],['','','']]
    for x in range (9):
        boards.append( [['','',''],['','',''],['','','']])


#player is identified by a character ('X' or 'O')
#check if player has won
    def win(self, player, boardNum):
        board = ""
        if(boardNum==10):
            board = self.bigBoard
        else:
            board = self.boards[boardNum]
        if(board[0]== [player,player,player]):
           board = [['','',''],['','',''],['','','']]
           return True
        if(board[1]== [player,player,player]):
           board = [['','',''],['','',''],['','','']]
           return True
        if(board[2]== [player,player,player]):
           board = [['','',''],['','',''],['','','']]
           return True
        if(board[0][0]== player and board[1][0]== player and board[2][0]== player):
           board = [['','',''],['','',''],['','','']]
           return True
        if(board[0][1]== player and board[1][1]== player and board[2][1]== player):
           board = [['','',''],['','',''],['','','']]
           return True
        if(board[0][2]== player and board[1][2]== player and board[2][2]== player):
           board = [['','',''],['','',''],['','','']]
           return True
        if(board[0][0]== player and board[1][1]== player and board[2][2]== player):
           board = [['','',''],['','',''],['','','']]
           return True
        if(board[0][2]== player and board[1][1]== player and board[2][0]== player):
           board = [['','',''],['','',''],['','','']]
           return True
        return False

#check if game has resulted in a draw
    def draw(self, player, boardNum):
        board = ""
        if(boardNum==10):
            board = self.bigBoard
        else:
            board = self.boards[boardNum]
        for x in range(9):
            if (board[(x//3)%3][x%3] == ""):
                return False
        return True


    def reset(self):
        self.bigBoard =  [['','',''],['','',''],['','','']]
        for x in range (9):
            self.boards[x] = ([['','',''],['','',''],['','','']])


#player moves, returns true if they win, check if cell is already taken
    def move(self,player,cell, boardNum):
        board = ""
        status = "good"
        if(boardNum==10):
            board = self.bigBoard
        else:
            board = self.boards[boardNum]


#if cell is already taken
        if(not board[(cell//3)%3][cell%3]==''):
            status = "bad 10"
            return status
        else:
            board[(cell//3)%3][cell%3] = player
#if board has been won already
        if(not self.bigBoard[(boardNum//3)%3][boardNum%3]==''):
            status = "bad 10"
            return status

# if sub-board is won, place move on bigboard
        if(self.win(player, boardNum)):
            status = ("win "+ str(boardNum))
            self.move(player,boardNum,10)
            if(self.win(player,10)):
                status = "win 10"
            elif(self.draw(player,10)):
                status = "draw 10"
# if sub-board has a Draw, place a "D" in bigboard, check if it's a draw
        if(self.draw(player, boardNum)):
            self.move("D",boardNum,10)
            if(self.draw(player,10)):
                status = "draw 10"
        return status

#for testing
    def gameLoop():
        x =game()

        for board in x.boards:
            print(board)
        print("Big")
        print(x.bigBoard)
        player = 'X'
        while(1):
            inp1, inp2 = input('Enter coordonates:').split()
            inp1 = int(inp1)
            inp2 = int(inp2)
            if(x.move(player,inp1,inp2)== "win"):
                print ("player "+player+" wins!!")
            if(player=='X'):
                player = 'O'

            elif(player=='O'):
                player = 'X'

            for board in x.boards:
                print(board)
            print("Big")
            print(x.bigBoard)
