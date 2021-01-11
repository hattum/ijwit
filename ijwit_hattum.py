from copy import deepcopy

eiwit = "HHPHHHPH"
eiwitten = "[HHPHHHPH] [HHPHHHPHPHHHPH] [HPHPPHHPHPPHPHHPPHPH] [HPHPPHHPHPPHPHHPPHPH]"

size = len(eiwit)
gridsize = size*2+1
grid = [ [ (-1,'_') for i in range(gridsize) ] for j in range(gridsize) ]
totalMoves = 1
currentPlace = (size, size)
grid[currentPlace[0]][currentPlace[1]] = (0,eiwit[0])

minimalScore = 0
minimalGrid = None

# grid[size-1][size] = (1,eiwit[1])
# grid[size-1][size-1] = (2,eiwit[2])
# grid[size][size-1] = (3,eiwit[3])
# grid[size+1][size-1] = (4,eiwit[4])
# grid[size+1][size] = (5,eiwit[5])
# grid[size+1][size+1] = (6,eiwit[6])
# grid[size][size+1] = (7,eiwit[7])



def printGrid(grid):
    for row in grid:
        print_list = []
        for tuble in row:
            print_list.append(str(tuble[0])+tuble[1])
        print(print_list)
    print()
    
def score(grid):
    score = 0
    for x in range(len(grid)-1):
        for y in range(len(grid)-1):
            if grid[x][y][1] == grid[x+1][y][1] == 'H':
               if grid[x][y][0] != grid[x+1][y][0]+1 and grid[x][y][0] != grid[x+1][y][0]-1:
                    score = score-1
            if grid[x][y][1] == grid[x][y+1][1] == 'H':
                if grid[x][y][0] != grid[x][y+1][0]+1 and grid[x][y][0] != grid[x][y+1][0]-1:
                    score = score-1

    return score
           
def checkPossibleMoves(grid, curtPlace):
    possiblemoves = []
    if grid[curtPlace[0]][curtPlace[1]+1][1] == '_':
        possiblemoves.append((curtPlace[0],curtPlace[1]+1))
    if grid[curtPlace[0]][curtPlace[1]-1][1] == '_':
        possiblemoves.append((curtPlace[0],curtPlace[1]-1))
    if grid[curtPlace[0]+1][curtPlace[1]][1] == '_':
        possiblemoves.append((curtPlace[0]+1,curtPlace[1]))
    if grid[curtPlace[0]-1][curtPlace[1]][1] == '_':
        possiblemoves.append((curtPlace[0]-1,curtPlace[1]))    
    return possiblemoves

def performMove(grid, move, totalMoves):
    grid[move[0]][move[1]] = (totalMoves, eiwit[totalMoves])
    return (totalMoves), move,




def recursion(grid, currentPlace, totalMoves):
    """This is a recursive function
    to find all possible folds"""

 
    if totalMoves == len(eiwit):
        global minimalScore, minimalGrid
        S = score(grid)
        if S < minimalScore:
            minimalScore = S
            minimalGrid = grid
            print(minimalScore)
            printGrid(grid)

        
    else:
        moves = checkPossibleMoves(grid,currentPlace)
        
        for move in moves:
            gridCopy = deepcopy(grid)
            
            totalMoves, currentPlace = performMove(gridCopy,move,totalMoves)
            recursion(gridCopy,currentPlace,totalMoves+1)

recursion(grid,currentPlace,totalMoves)


print("Print minimal grid")
printGrid(minimalGrid)

print(minimalScore)