# imports
import random
from copy import deepcopy

from Jeroen.classes.visualisation_OOP import Visualisation

class Grid:
    """
    Grid initializes the grid space where the protein will be folded in.
    Grid prints the grid as a list of lists.
    Grid calculates the score of the folded protein.
    Grid checks the possible folding moves for the protein.
    Grid performs specific folding moves.
    """
    def  __init__(self, size):
        actualgridsize = 2*size + 1
        self.content = [ [ (-1,'_') for i in range(actualgridsize) ] for j in range(actualgridsize) ]
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
        


class Protein:
    """
    Protein returns the subsequent letters
    of the amino acid sequence one by one(queue).
    """
    def __init__(self, code):
        self.code = code
        self.length = len(code)

    def pop_first_char(self):
        """
        Returns the first amino acid in the list.
        """
        letter = self.code[0]
        self.code = self.code[1:]
        self.length = len(self.code)
        return letter


## HPHPPHHPHPPHPHHPPHPH
moveList = []

# initialize a Protein object called protein
protein = Protein("HPHPPHHPHP")

# initialize a Grid object called grid
grid = Grid(protein.length)

# append all the possible folding moves to the list moveList
moveList.append(grid.checkPossibleMoves()[0])

# places the amino acids in the grid on their calculated place
grid.performMove(grid.checkPossibleMoves()[0], protein.pop_first_char())

"""
# while protein.length > 0:
#     moves = grid.checkPossibleMoves()
#     letter = protein.pop_first_char()
#     grid.performMove(random.choice(moves),letter)
"""




# HPHPPHHPHPPHPHHPPHPH
allMoves = []
protein = Protein("HPHPPHHPHPPHPHHPPHPH")
length = protein.length
grid = Grid(length)
minimalScore = 0
minimalGrid = None
minimalPerformedMove = None
recursionAmount = 0


def recursion(grid, protein, depth, firstMove):
    """
    Recursion tries to find all possible foldings of 
    the protein by looking a set steps(depth) ahead.
    """

    global minimalScore, minimalGrid, minimalPerformedMove, recursionAmount

    # print the amount of recursions for convenience purposes
    if (recursionAmount % 10000 )== 0:
        print(recursionAmount)
    recursionAmount = recursionAmount+1

    # 
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

        # check the possible moves
        moves = grid.checkPossibleMoves()
        
        for move in moves:

            # try every possible move by using a deepcopy of the grid & protein
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
            minimalPerformedMove = firstMove
            
    else:
        moves = grid.checkPossibleMoves()
        for move in moves:
            allMoves = allMoves[:(depth+(numberOfPerformedMoves))]
            allMoves.append(move)
            grid = Grid(length)
            for allMove in allMoves:
                
                grid.performMove(allMove, protein.code[grid.totalMoves])
            
            if depth == 0:
                recursion_01(grid, allMoves, depth+1, length, move, numberOfPerformedMoves)
            else:
                recursion_01(grid, allMoves, depth+1, length, firstMove, numberOfPerformedMoves)
            

letterPos = 0
while protein.length > letterPos:
    recursion_01(grid, allMoves, 0, length, None, letterPos)
    allMoves.append(minimalPerformedMove)
    grid.performMove(minimalPerformedMove, protein.code[letterPos])
    minimalPerformedMove = None
    minimalScore = 0
    letterPos = letterPos +1
    print(letterPos)

print(grid.score())
grid.printGrid()
# print(minimalScore)
# grid.printGrid()