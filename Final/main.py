#imports
from classes_hattum import grid_c, grid, protein
from algorithms_hattum import greedy_lookahead
from  visualisation import Visualisation



if __name__ == "__main__":

    # set the amino string you want to fold
<<<<<<< HEAD
    amino_string = "HPHPPHHPHPPHPHHPPHPH"
=======
    #amino_string = "HHPHHHPHPHHHPH"
    #amino_string = "HPHPPHHPHPPHPHHPPHPH"
    #amino_string = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
    #amino_string = "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"

    amino_string = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
    #amino_string = "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC"
    #amino_string = "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH"
    #amino_string = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"

    # set the number of steps to look ahead
    steps = 5
>>>>>>> 992f9964b61d41b6bbc75e58272ae72b0dc88af8


    protein = protein.Protein(amino_string)

    # choose to use grid.py or grid_c.py
    #grid = grid.Grid(protein.length)
    grid = grid_c.Grid_c(protein.length)

    print(type(grid))
<<<<<<< HEAD
    algo = greedy_lookahead.Greedy_lookahead(protein,grid,9)
=======
    algo = greedy_lookahead.Greedy_lookahead(protein, grid, steps)
>>>>>>> 992f9964b61d41b6bbc75e58272ae72b0dc88af8

    # plots the folded protein in a grid
    visualisation = Visualisation(amino_string, grid.score(), algo.allMoves)
    visualisation.plot()
