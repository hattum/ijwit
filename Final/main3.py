#imports
from assets.helpers_miro import offsets, eiwitDict
from classes_hattum.queue_miro import Queue
from classes_hattum.fold_miro import Fold, PriorityFold, CycleFold
from classes_hattum import grid, protein
from algorithms_hattum import greedy_lookahead, random_valid
from visualisation import Visualisation



if __name__ == "__main__":

    # print eiwit-options
    print("eiwit-options:")
    for key, value in eiwitDict.items():
        print(key,': ', value[0])

    # Get choices from the user regarding eiwit-options and algorithm
    option = input("make an option: ")
    while True:
        if option == '9':
            exit()
        elif option in eiwitDict:
            eiwit = eiwitDict[option][0]
            heuristic = eiwitDict[option][1]
            break
        else:
            print("You did not enter a valid number")
            option = input("make an option: ")


    choice = input("Would you like to use cyclefold (C) or priority (P) or Greedy_Lookahead (G) or random_valid (R)?: ")
    if choice.lower() == "cyclefold" or choice.upper() == "C":
        # Initialize the needed class for the algo
        fold = CycleFold(eiwit)

        # Plot the folded protein in a grid after getting coordinates and scoreH
        scoreH = fold.score()
        coordinates = fold.coord()
        visualisation = Visualisation(eiwit, scoreH, coordinates)
        visualisation.plot()
        visualisation.csv()

    elif choice.lower() == "priority" or choice.upper() == "P":
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
                    print(f"Depth must be between 3 and {len(eiwit)}")
        
        # Make cyclevalue which is used in heuristics and related to depth/length
        cyclefold = CycleFold(depth * "H")
        cyclevalue = cyclefold.score()

        # Initialize the needed class for the algo
        fold = PriorityFold(eiwit, depth, cyclevalue, heuristic)

        # Plot the folded protein in a grid after getting winner and scoreH
        winner, scoreH = fold.score()
        visualisation = Visualisation(eiwit, scoreH, winner)
        visualisation.plot()
        visualisation.csv()

    elif choice.lower() == "greedy_lookahead" or choice.upper() == "G":
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
<<<<<<< HEAD

        # Making de csv output file
        visualisation.directions()
=======
        visualisation.csv()

    elif choice.lower() == "random_valid" or choice.upper() == "R":
        protein = protein.Protein(eiwit)
        grid = grid.Grid(protein.length) 

        tries = int(input("How many times would you like to try to find the best random solution: "))
        algo = random_valid.Random_valid(grid, protein, tries)
        visualisation = Visualisation(eiwit, grid.score(), algo.allMoves)
        visualisation.plot()
>>>>>>> 40c567711b3a9e0cd57a6f843f0219361d4bf483
        visualisation.csv()
    