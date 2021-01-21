#imports
from assets.helpers_miro import offsets
from queue_miro import Queue
from fold_miro import Fold, PriorityFold, CycleFold
from classes_hattum import grid_c, grid, protein
from algorithms_hattum import greedy_lookahead
from visualisation import Visualisation
from visualisation_X import Visualisation_X

if __name__ == "__main__":

    print("""eiwit-options:
    _______________________________
    0: HHPHHHPH
    1: HHPHHHPHPHHHPH
    2: HPHPPHHPHPPHPHHPPHPH
    3: PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP
    4: HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH
    5: PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP
    6: CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC
    7: HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH
    8: HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH
    9: exit program
    """)

    option2 = int(input("make an option: "))
    if option2 == 0:
        eiwit = "HHPHHHPH"
    elif option2 == 1:
        eiwit = "HHPHHHPHPHHHPH"
    elif option2 == 2:
        eiwit = "HPHPPHHPHPPHPHHPPHPH"
    elif option2 == 3:
        eiwit = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
    elif option2 == 4:
        eiwit = "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"
    elif option2 == 5:
        eiwit = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
    elif option2 == 6:
        eiwit = "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC"
    elif option2 == 7:
        eiwit = "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH"
    elif option2 == 8:
        eiwit = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"
    elif option2 != 9:
        print("You did not enter a valid number")

        option2 = int(input("make an option: "))
    else:
        print("Ends")

    option = input("Would you like to use cyclefold (C) or priority (P) or Greedy_Lookahead (G)?: ")
    if option.lower() == "cyclefold" or option.upper() == "C":
        algorithm = "cyclefold"
        fold = CycleFold(eiwit, algorithm)

        fold.plot()

        fold.printDirections()

        scoreH = fold.score()
        print("\nScoreH is:", scoreH)
    elif option.lower() == "priority" or option.upper() == "P":
        algorithm = "priority"
        print("""Depth info:
             _______________________________
             If you are a developer you can set a depth after you answered 'yes' (Y).
             Otherwise just say 'no' (N).
             """)
        option = input("Would you like to set a depth?: ")
        if option.lower() == "no" or option.upper() == "N":
            depth = len(eiwit)
        if option.lower() == "yes" or option.upper() == "Y":
            while True:
                depth = int(input("\nWhich depth would you like to explore?: "))
                if depth > 2 and depth <= len(eiwit):
                    break
                else:
                    print("Depth between 3 and eiwit-length")

        fold = PriorityFold(eiwit, algorithm, depth)
        winner, scoreH = fold.score()
        print("\nBestChild is:", winner)
        print("BestScore is:", scoreH)
    elif option.lower() == "greedy_lookahead" or option.upper() == "G":
        steps = int(input("How for would you like to lookahead: "))
        protein = protein.Protein(eiwit)

        # choose to use grid.py or grid_c.py
        grid = grid.Grid(protein.length)
        
        algo = greedy_lookahead.Greedy_lookahead(protein, grid, steps)

        # plots the folded protein in a grid
        visualisation = Visualisation(amino_string, grid.score(), algo.allMoves)
        visualisation.plot()
        visualisation.csv()
    