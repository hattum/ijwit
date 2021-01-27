#imports
from assets.helpers_miro import offsets, eiwitDict
from classes.queue_miro import Queue
from classes.cyclefold import CycleFold
from classes.priorityfold import PriorityFold
from classes import grid, protein
from algorithms import greedy_lookahead, random_valid
from classes.visualisation import Visualisation



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
        fold.run()

        # Variables for the plot
        score = fold.score()
        coordinates = fold.coord()
        print("Score is:", score)


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
        cyclefold.run()
        cyclevalue = cyclefold.score()

        # Initialize the needed class for the algo
        fold = PriorityFold(eiwit, depth, cyclevalue, heuristic)

        fold.run()

        # Variables for the plot
        coordinates, score = fold.score()
        print("A best score is:", score)

        
        

    elif choice.lower() == "greedy_lookahead" or choice.upper() == "G":
        # Lookahead count
        steps = int(input("How for would you like to lookahead: "))

        # Initializing the needed classes for the algo
        protein = protein.Protein(eiwit)
        grid = grid.Grid(protein.length)

        # Performing the greedy algo with lookahead
        algo = greedy_lookahead.Greedy_lookahead(protein, grid, steps)

        # Variables for the plot
        score = grid.score()
        coordinates = algo.allMoves


    elif choice.lower() == "random_valid" or choice.upper() == "R":
        # Initializing the needed classes for the algo
        protein = protein.Protein(eiwit)
        grid = grid.Grid(protein.length) 

        tries = int(input("How many times would you like to try to find the best random solution: "))
        # Performing the random algo 'tries' times
        algo = random_valid.Random_valid(grid, protein, tries)

        # Variables for the plot
        score = grid.score()
        coordinates = algo.allMoves

 
    # Plot the folded protein in a grid
    visualisation = Visualisation(eiwit, score, coordinates)
    visualisation.plot()

    # Making de csv output file
    visualisation.directions()
    visualisation.csv()

    