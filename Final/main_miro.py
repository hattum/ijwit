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
    6: CPPCHPPCHPPCPPHHHHHHCCPCHPPC PCHP PHPC
    7: HCPH PCPH PCHC HPHP PPHP PPHP PPPH PC PH PPPHPHHHCCHCHCHCHH
    8: HCPH PHPH CHHH HPCC PPHP PPHP PPPC PPPH PPPH PHHH HCHPH PHPHH
    9: exit program
    """)

    option2 = int(input("make an option: "))
    if option2 == 0:
        eiwit = "HHPHHHPH"
        #eiwit = "CHHCHCHC"
        #eiwit = "H" *20
    elif option2 == 1:
        eiwit = "HHPHHHPHPHHHPH"
    elif option2 == 2:
        eiwit = "HPHPPHHPHPPHPHHPPHPH" #20
    elif option2 == 3:
        eiwit = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP" #36
    elif option2 == 4:
        eiwit = "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH" #50
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

    option = input("Would you like to use cyclefold (C) or priority (P) or Hattum (H)?: ")
    if option.lower() == "cyclefold" or option.upper() == "C":
        algorithm = "cyclefold"
        fold = CycleFold(eiwit, algorithm)

        #fold.plot()

        #fold.printDirections()

        scoreH = fold.score()
        print("\nScoreH is:", scoreH)

        coordinates = fold.coord()
        print("Coordinates are:", coordinates)

        # visualisation = Visualisation(eiwit, scoreH, coordinates)
        # visualisation.plot()
        

    # scoreHvar = fold.scoreHvar()
    # print("\nScoreHvar is:", scoreHvar)

    # scoreC = fold.scoreC()
    # print("\nScoreC is:", scoreC)

        
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
        cyclefold = CycleFold(depth * "H", algorithm) #nieuw
        cyclevalue = cyclefold.score()  #nieuw

        # print("\nCyclevalue is:", cyclevalue)
        #fold = PriorityFold(eiwit, algorithm, depth)
        fold = PriorityFold(eiwit, algorithm, depth, cyclevalue)
        
        scoorders, scoreY = fold.score()
        print("\nBestChilds are:", scoorders)
        print("BestScore is:", scoreY)
        print("\nCyclevalue is:", cyclevalue)

        #winner, scoreH = fold.score()
        #print("\nBestChild is:", winner)
        #print("BestScore is:", scoreH)

        #TODO: visualisation = Visualisation(title, scoreH, winner)
        #? visualisation.plot()
  
if __name__ == "__main__":
    main()

    # print("\nCurrAmi: Richting")
    # for tupler in range(len(directions2)):
    #     print(directions2[tupler][0], ",", directions2[tupler][1])

    #H_q = fold.makeH_q()

    #H_lijst = fold.makeH_lijst()
    #print("H_lijst is:", H_lijst)

    #C_q = fold.makeC_q()

    #C_lijst = fold.makeC_lijst()
    #print("\nC_lijst is:", C_lijst)

    # print("\nDirections2:")
    # print(directions2)

    # print("\nAmino_posities:")
    # print(amino_path)

    # print("\nPosition: Predecessor")
    # for pos in predecessors:
    #     print(pos, ":" , predecessors[pos])

    # print("\nPositie: Amino")
    # for amino in match:
    #     print(amino, ":" , match[amino])
 
    # print("\nCurrPos: Richting")
    # for pos in directions:
    #     print(pos, ":" , directions[pos])
    

