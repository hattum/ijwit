#imports
from classes_hattum import grid, protein
from algorithms_hattum import greedy_lookahead
from  visualisation import Visualisation



if __name__ == "__main__":

    # set the amino string you want to fold
    amino_string = "HPHPPHHPHPPHPHHPPHPH"


    protein = protein.Protein(amino_string)
    grid = grid.Grid(protein.length)
    print(type(grid))
    algo = greedy_lookahead.Greedy_lookahead(protein,grid,9)

    # plots the folded protein in a grid
    visualisation = Visualisation(amino_string, grid.score(), algo.allMoves)
    visualisation.plot()
