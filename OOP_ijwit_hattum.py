import random
from copy import deepcopy

from Jeroen.classes.visualisation_OOP import Visualisation

class Grid:
    def  __init__(self, size):
        actualgridsize = 2*size + 1
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
        


class Protein:
    def __init__(self, code):
        self.code = code
        self.length = len(code)

    def pop_first_char(self):
        letter = self.code[0]
        self.code = self.code[1:]
        self.length = len(self.code)
        return letter
## HPHPPHHPHPPHPHHPPHPH
moveList = []
protein = Protein("HPHPPHHPHP")
grid = Grid(protein.length)
moveList.append(grid.checkPossibleMoves()[0])
grid.performMove(grid.checkPossibleMoves()[0], protein.pop_first_char())
# while protein.length > 0:
#     moves = grid.checkPossibleMoves()
#     letter = protein.pop_first_char()
#     grid.performMove(random.choice(moves),letter)




minimalScore = 0
minimalGrid = None
minimalPerformedMove = None
recursionAmount = 0


def recursion(grid, protein, depth, firstMove):
    """This is a recursive function
    to find all possible folds"""

    global minimalScore, minimalGrid, minimalPerformedMove, recursionAmount
    if (recursionAmount % 10000 )== 0:
        print(recursionAmount)
    recursionAmount = recursionAmount+1

    if depth == 99 or protein.length == 0:
        #depth = 0
        S = grid.score()
        # print("score = "+ str(S)+ "minimal= "+ str(minimalScore))
        if S <= minimalScore and (len(grid.checkPossibleMoves()) > 0 or protein.length == 0):
            minimalScore = S
            minimalGrid = grid
            minimalPerformedMove = firstMove
            # print(minimalScore)
            # grid.printGrid()
         
    else:
        moves = grid.checkPossibleMoves()
        
        for move in moves:

            gridCopy = deepcopy(grid)
            proteinCopy = deepcopy(protein)
            letter = proteinCopy.pop_first_char()
            gridCopy.performMove(move,letter)
            if depth == 0:
                recursion(gridCopy,proteinCopy,depth+1, move)
            else:
                recursion(gridCopy,proteinCopy,depth+1, firstMove)


while protein.length > 0:

    recursion(grid,protein,0,None)
    moveList.append(minimalPerformedMove)
    
    
    grid.performMove(minimalPerformedMove, protein.pop_first_char())
    minimalPerformedMove = None
    

    print(protein.length)

print(f'move list: {moveList}')
visualisation = Visualisation("HPHPPHHPHPPHPHHPPHPH", grid.score(), moveList)
visualisation.plot()

print(moveList)

print(f"grid scor: {grid.score()}")
grid.printGrid()

######### 2.0

allMoves = []
protein = Protein("HPHPPHHPHP")
grid = Grid(10)
minimalScore = 0
minimalGrid = None
minimalPerformedMove = None
   
def recursion_01(grid, allMoves, depth):
    """This is a recursive function
    to find all possible folds"""

    global minimalScore, minimalGrid
    

    if depth == 10 or protein.length == 0:
        S = grid.score()
        if S <= minimalScore and (len(grid.checkPossibleMoves()) > 0 or protein.length == 0):
            minimalScore = S
            minimalGrid = grid
            
         
    else:
        
        moves = grid.checkPossibleMoves()
        for move in moves:
            allMoves = allMoves[:depth]
            allMoves.append(move)
            grid = Grid(10)
            for allMove in allMoves:
                grid.performMove(allMove, protein.code[grid.totalMoves])
            
            
            recursion_01(grid, allMoves, depth+1)

    

recursion_01(grid, allMoves, 0)

print(minimalScore)
minimalGrid.printGrid()