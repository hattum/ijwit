#imports
from classes_hattum import grid, grid, protein
from algorithms_hattum import greedy_lookahead
from visualisation import Visualisation
from visualisation_X import Visualisation_X



if __name__ == "__main__":

    # set the amino string you want to fold
    #amino_string = "HHPHHHPHPHHHPH"
    #amino_string = "HPHPPHHPHPPHPHHPPHPH"
    #amino_string = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
    #amino_string = "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"

    amino_string = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
    #amino_string = "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC"
    #amino_string = "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH"
    #amino_string = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"

    # set the number of steps to look ahead
    steps = 3


    protein = protein.Protein(amino_string)

    # choose to use grid.py or grid_c.py
    grid = grid.Grid(protein.length)
    

    
    algo = greedy_lookahead.Greedy_lookahead(protein, grid, steps)
    print(algo.allMoves)

    # plots the folded protein in a grid
    visualisation = Visualisation(eiwit, grid.score(), algo.allMoves)
    visualisation.plot()
    visualisation.csv()
