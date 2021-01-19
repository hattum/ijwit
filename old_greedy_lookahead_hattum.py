from copy import deepcopy
from classes_hattum.protein import Protein
from classes_hattum.grid import Grid

from Jeroen.classes.visualisation_OOP import Visualisation



## HPHPPHHPHPPHPHHPPHPH
moveList = []

# initialize a Protein object called protein
protein = Protein("PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP")
length = protein.length

# initialize a Grid object called grid
grid = Grid(length)

# append all the possible folding moves to the list moveList
moveList.append(grid.checkPossibleMoves()[0])

# places the amino acids in the grid on their calculated place
grid.performMove(grid.checkPossibleMoves()[0], protein.pop_first_char())

## HPHPPHHPHPPHPHHPPHPH

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
    if depth == 2 or protein.length == 0:
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




