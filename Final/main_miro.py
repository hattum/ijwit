from assets.helpers_miro import offsets
from classes_hattum.fold_miro import PriorityFold, CycleFold
from visualisation import Visualisation

def main():

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
        heuristic = "admissable"
    elif option2 == 1:
        eiwit = "HHPHHHPHPHHHPH"
        heuristic = "admissable"
    elif option2 == 2:
        eiwit = "HPHPPHHPHPPHPHHPPHPH"
        heuristic = "regular"
    elif option2 == 3:
        eiwit = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
        heuristic = "cyclebased"
    elif option2 == 4:
        eiwit = "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"
        heuristic = "cyclebased"
    elif option2 == 5:
        eiwit = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"
        heuristic = "regular"
    elif option2 == 6:
        eiwit = "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC"
        heuristic = "cyclebased"
    elif option2 == 7:
        eiwit = "HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH"
        heuristic = "cyclereducedbyfactor"
    elif option2 == 8:
        eiwit = "HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH"
        heuristic = "cyclebased"
    elif option2 != 9:
        print("You did not enter a valid number")

        option2 = int(input("make an option: "))
    else:
        print("Ends")

    option = input("Would you like to use cyclefold (C) or priority (P) or Hattum (H)?: ")
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
                    print("Depth between 3 and eiwit-length")
        cyclefold = CycleFold(depth * "H")
        cyclevalue = cyclefold.score()
        fold = PriorityFold(eiwit, depth, cyclevalue, heuristic)
        #scoorders, scores = fold.scoorders()
        winner, scoreH = fold.score()
        visualisation = Visualisation(eiwit, scoreH, winner)
        visualisation.plot()
        #visualisation.csv()
  
if __name__ == "__main__":
    main()

    

