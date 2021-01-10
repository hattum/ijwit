import random

class Grid:
    def  __init__(self, size):
        actualgridsize = 2*size + 1
        self.content = [ [ (-1,'_') for i in range(actualgridsize) ] for j in range(actualgridsize) ]
        self.currentPlace = (size,size)
        self.totalMoves = 0

    def printGrid(self,printForm):
        for row in self.content:
            print_list = []
            for tuble in row:
                print_list.append(tuble[printForm])
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
        return


class Protein:
    def __init__(self, code):
        self.code = code
        self.length = len(code)

    def pop_first_char(self):
        letter = self.code[0]
        self.code = self.code[1:]
        self.length = len(self.code)
        return letter
        

protein = Protein("HHPHHHPH")
grid = Grid(protein.length)
while protein.length > 0:
    moves = grid.checkPossibleMoves()
    letter = protein.pop_first_char()
    grid.performMove(random.choice(moves),letter)


grid.printGrid(1)
print(grid.score())
