from copy import deepcopy
from classes_hattum.protein import Protein
from classes_hattum.grid import Grid

from Jeroen.classes.visualisation_OOP import Visualisation


## HPHPPHHPHPPHPHHPPHPH

moveList = []
protein = Protein("HPHPPHHPHPP")
length = protein.length
grid = Grid(length)
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

    if depth == 3 or protein.length == 0:
        S = grid.score()
        if S <= minimalScore and (len(grid.checkPossibleMoves()) > 0 or protein.length == 0):
            minimalScore = S
            minimalGrid = grid
            minimalPerformedMove = firstMove
         
        
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
moveList = [(a-length,b-length) for a,b in moveList]
print(moveList)
visualisation = Visualisation("HPHPPHHPHPPHPHHPPHPH", grid.score(), moveList)
visualisation.plot()

print(moveList)

print(f"grid scor: {grid.score()}")
grid.printGrid()
