#imports
from assets.helpers_miro import offsets
from classes_hattum.queue_miro import Queue
from classes_hattum.fold_miro import Fold, PriorityFold, CycleFold
from classes_hattum import grid, protein
from algorithms_hattum import greedy_lookahead
from visualisation import Visualisation



if __name__ == "__main__":
    eiwitDict = {
        '0':["HHPHHHPH", "admissable"],
        '1':["HHPHHHPHPHHHPH", "admissable"],
        '2':["HPHPPHHPHPPHPHHPPHPH", "regular"],
        '3':["PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP", "cyclebased"],
        '4':["HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "cyclebased"],
        '5':["PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP", "regular"],
        '6':["CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC", "cyclebased"],
        '7':["HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH", "cyclereducedbyfactor"],
        '8':["HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH", "cyclebased"]
    }

    print("eiwit-options:")
    for key, value in eiwitDict.items():
        print(key,': ', value[0])

    # Choice menu for the different Protien
    option2 = input("make an option: ")
    while True:
        if option2 == '9':
            exit()
        elif option2 in eiwitDict:
            eiwit = eiwitDict[option2][0]
            heuristic = eiwitDict[option2][1]
            break
        else:
            print("You did not enter a valid number")
            option2 = input("make an option: ")


    option = input("Would you like to use cyclefold (C) or priority (P) or Greedy_Lookahead (G)?: ")
    if option.lower() == "cyclefold" or option.upper() == "C":

        fold = CycleFold(eiwit)
        #fold.printDirections()
        scoreH = fold.score()
        coordinates = fold.coord()
        visualisation = Visualisation(eiwit, scoreH, coordinates)
        visualisation.plot()

    elif option.lower() == "priority" or option.upper() == "P":
        algorithm = "priority"
        print("""\nDepth info: By setting a depth you can examine the proteine from the
             first amino upto the set depth
             _______________________________
             Type 'no' (N) if you don't understand this depth option or if you just want to examine the whole proteine.
             Type 'yes' (Y) if you want to set the depth.
             """)
        option = input("\nWould you like to set a depth?: ")
        if option.lower() == "no" or option.upper() == "N":
            depth = len(eiwit)
        if option.lower() == "yes" or option.upper() == "Y":
            while True:
                depth = int(input("\nWhich depth would you like to explore?: "))
                if depth > 2 and depth <= len(eiwit):
                    break
                else:
                    print("Depth must be between 3 and eiwit-length")
        cyclefold = CycleFold(depth * "H")
        cyclevalue = cyclefold.score()
        fold = PriorityFold(eiwit, depth, cyclevalue, heuristic)
        #scoorders, scores = fold.scoorders()
        winner, scoreH = fold.score()
        print("Winner is:", winner)
        directs = directions(winner)
        print("Directions are:", directs)

        visualisation = Visualisation(eiwit, scoreH, winner)
        visualisation.plot()
        
        #visualisation.csv()

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
        visualisation.directions()
        visualisation.csv()
    