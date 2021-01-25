#imports
from assets.helpers_miro import offsets
from classes_hattum.queue_miro import Queue
from classes_hattum.fold_miro import Fold, PriorityFold, CycleFold
from classes_hattum import grid, protein
from algorithms_hattum import greedy_lookahead
from visualisation import Visualisation


if __name__ == "__main__":
    eiwitDict = {
        '0':"HHPHHHPH",
        '1':"HHPHHHPHPHHHPH",
        '2':"HPHPPHHPHPPHPHHPPHPH",
        '3':"PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP",
        '4':"HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH",
        '5':"PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP",
        '6':"CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC",
        '7':"HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH",
        '8':"HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH",
    }

    print("eiwit-options:")
    for key, value in eiwitDict.items():
        print(key,': ', value)

    # Choice menu for the different Protien
    option2 = input("make an option: ")
    while True:
        if option2 == '9':
            exit()
        elif option2 in eiwitDict:
            eiwit = eiwitDict[option2]
            break
        else:
            print("You did not enter a valid number")
            option2 = input("make an option: ")


    option = input("Would you like to use cyclefold (C) or priority (P) or Greedy_Lookahead (G)?: ")
    if option.lower() == "cyclefold" or option.upper() == "C":
        algorithm = "cyclefold"
        fold = CycleFold(eiwit, algorithm)
        scoreH = fold.score()
        coordinates = fold.coord()
        visualisation = Visualisation(eiwit, scoreH, coordinates)
        visualisation.plot()
      
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
        # Lookahead count
        steps = int(input("How for would you like to lookahead: "))

        # Initializing the needed classes for the algo
        protein = protein.Protein(eiwit)
        grid = grid.Grid(protein.length)

        # Performing the greedy algo with lookahead
        algo = greedy_lookahead.Greedy_lookahead(protein, grid, steps)
        
        # Plot the folded protein in a grid
        visualisation = Visualisation(eiwit, grid.score(), algo.allMoves)
        visualisation.plot()
        visualisation.csv()
    