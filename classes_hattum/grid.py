class Grid:
    def  __init__(self, size):
        actualgridsize = 2*size + 2
        self.content = [ [ (-1,'_') for i in range(actualgridsize) ] for j in range(actualgridsize) ]
        self.currentPlace = (size,size)
        self.totalMoves = 0
        

    def printGrid(self):
        for row in self.content:
            print_list = []
            for tuble in row:
                print_list.append(str(tuble[0])+tuble[1])
            print(print_list)
        print()

    def score(self):
        score = 0
        for x in range(len(self.content)-1):
            for y in range(len(self.content)-1):
                if self.content[x][y][1] == self.content[x+1][y][1] == 'H':
                    if self.content[x][y][0] != self.content[x+1][y][0]+1 and self.content[x][y][0] != self.content[x+1][y][0]-1:
                            score = score-1
                if self.content[x][y][1] == self.content[x][y+1][1] == 'H':
                    if self.content[x][y][0] != self.content[x][y+1][0]+1 and self.content[x][y][0] != self.content[x][y+1][0]-1:
                        score = score-1

        return score

    def checkPossibleMoves(self):
        possiblemoves = []
        if self.totalMoves == 0:
            possiblemoves.append((self.currentPlace[0],self.currentPlace[1]))         
        else:
            if self.content[self.currentPlace[0]][self.currentPlace[1]+1][1] == '_':
                possiblemoves.append((self.currentPlace[0],self.currentPlace[1]+1))
            if self.content[self.currentPlace[0]][self.currentPlace[1]-1][1] == '_':
                possiblemoves.append((self.currentPlace[0],self.currentPlace[1]-1))
            if self.content[self.currentPlace[0]+1][self.currentPlace[1]][1] == '_':
                possiblemoves.append((self.currentPlace[0]+1,self.currentPlace[1]))
            if self.content[self.currentPlace[0]-1][self.currentPlace[1]][1] == '_':
                possiblemoves.append((self.currentPlace[0]-1,self.currentPlace[1]))    
        return possiblemoves

    def performMove(self, move, letter):
        self.content[move[0]][move[1]] = (self.totalMoves, letter)
        self.currentPlace = (move[0], move[1])
        self.totalMoves = self.totalMoves + 1
        
