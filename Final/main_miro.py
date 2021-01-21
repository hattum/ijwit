from helpers_miro import offsets
from queue_miro import Queue
from fold_miro import Fold, PriorityFold, CycleFold

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

    option = input("Would you like to use cyclefold (C) or priority (P) or Hattum (H)?: ")
    if option.lower() == "cyclefold" or option.upper() == "C":
        algorithm = "cyclefold"
        fold = CycleFold(eiwit, algorithm)
    

        fold.plot()

        fold.printDirections()

        scoreH = fold.score()
        print("\nScoreH is:", scoreH)

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

        fold = PriorityFold(eiwit, algorithm, depth)
        winner, scoreH = fold.score()
        print("\nBestChild is:", winner)
        print("BestScore is:", scoreH)
  
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
    

