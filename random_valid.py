from classes_hattum.protein import Protein
from classes_hattum.grid import Grid
import random

x = 0
globalscore = 1
globalgrid = None

while x < 10000:
    protein = Protein("HPHPPHHPH")
    grid = Grid(protein.length)
    grid.performMove(grid.checkPossibleMoves()[0], protein.pop_first_char())
    while protein.length > 0:
        moves = grid.checkPossibleMoves()
        if len(moves) == 0:
            break
        letter = protein.pop_first_char()
        grid.performMove(random.choice(moves),letter)
    if grid.score() < globalscore:
        print(grid.score())
        globalscore = grid.score()
        globalgrid = grid
        globalgrid.printGrid()
    x = x+1

