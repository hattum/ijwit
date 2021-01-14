#from helpers_miro import offsets, cyclesearch, Aminostring
# from helpers_miro import offsets, Aminostring
from helpers_miro import offsets
#from queue_miro_backup import Queue, AminoQueue
from queue_miro import Queue, AminoQueue
from fold_miro import Fold

def main():

    algorithm = "cyclefold"
    eiwit = "HHPHHHPH"

    #eiwit = "HHPHHHPH"
    #eiwit = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
    #eiwit = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"

    fold = Fold(eiwit, algorithm) #nieuw
    #fold = Fold(eiwit)
    fold.plot()

    fold.printDirections()

    scoreH = fold.scoreH()
    print("\nScoreH is:", scoreH)

    # scoreHvar = fold.scoreHvar()
    # print("\nScoreHvar is:", scoreHvar)

    scoreC = fold.scoreC()
    print("\nScoreC is:", scoreC)

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
    

