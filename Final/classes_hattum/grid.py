class Grid:
    """
    Grid initializes the grid space where the protein will be folded in.
    Grid prints the grid as a list of lists.
    Grid calculates the score of the folded protein.
    Grid checks the possible folding moves for the protein.
    Grid performs specific folding moves.
    """
    def  __init__(self, size):
        self.actualgridsize = 2*size + 1
        self.content = [ [ (-1,'_') for i in range(self.actualgridsize) ] for j in range(self.actualgridsize) ]
        self.currentPlace = (size,size)
        self.totalMoves = 0
        

    def printGrid(self):
        """
        Prints the grid as a list of lists.
        """
        for row in self.content:
            print_list = []
            for tuble in row:
                print_list.append(str(tuble[0])+tuble[1])
            print(print_list)
        print()

    def score(self):
        """
        Checks whether amino acids lay next to each other that can bond,
        and returns the corresponding score.
        """
        score = 0
        for x in range(len(self.content)-1):
            for y in range(len(self.content)-1):
                if self.content[x][y][1] == self.content[x+1][y][1] == 'H':
                    if self.content[x][y][0] != self.content[x+1][y][0]+1 and self.content[x][y][0] != self.content[x+1][y][0]-1:
                            score = score-1
                if self.content[x][y][1] == self.content[x][y+1][1] == 'H':
                    if self.content[x][y][0] != self.content[x][y+1][0]+1 and self.content[x][y][0] != self.content[x][y+1][0]-1:
                        score = score-1
                if self.content[x][y][1] == self.content[x+1][y][1] == 'C':
                    if self.content[x][y][0] != self.content[x+1][y][0]+1 and self.content[x][y][0] != self.content[x+1][y][0]-1:
                            score = score-5
                if self.content[x][y][1] == self.content[x][y+1][1] == 'C':
                    if self.content[x][y][0] != self.content[x][y+1][0]+1 and self.content[x][y][0] != self.content[x][y+1][0]-1:
                        score = score-5

        return score

    def checkPossibleMoves(self):
        """
        Makes a list of all the possible folding moves for the next folding step.
        """
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
        """
        Places the amino acids in the grid on their calculated place.
        """
        self.content[move[0]][move[1]] = (self.totalMoves, letter)
        self.currentPlace = (move[0], move[1])
        self.totalMoves = self.totalMoves + 1
      
    def clearGrid(self):
        self.content = [ [ (-1,'_') for i in range(self.actualgridsize) ] for j in range(self.actualgridsize) ]
        self.totalMoves = 0