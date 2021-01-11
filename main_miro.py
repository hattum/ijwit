#from helpers_miro import offsets, cyclesearch, Aminostring
# from helpers_miro import offsets, Aminostring
from helpers_miro import offsets
from queue_miro import Queue, AminoQueue

def main():

    scoreH = 0
    scoreC = 0

    match = {}

    eiwit = "HHPHHHPH"
    #eiwit = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
    #eiwit = "PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP"

    amino_q = AminoQueue(eiwit)

    graph = [["   " for i in range(len(eiwit))] for i in range(len(eiwit))]
    #graph = [["   " for i in range(int(len(eiwit)/4))] for i in range(int(len(eiwit)/4))]

    amino_path, predecessors, directions, directions2 = amino_q.cyclefold()

    # score = amino_q.score()
    # print("Score is:", score)

    for j, element in enumerate(zip(amino_path, list(eiwit))):
        pos = element[0]
        amino = element[1]
        match[pos] = amino
        graph[pos[0]][pos[1]] = amino+str(j)
        #graph[pos[0]][pos[1]] = amino

    print("\nPositie: Amino-H")
    H_q = Queue()
    for amino in match:
        if match[amino] == "H":
            print(amino, ":" , match[amino])
            H_q.enqueue(amino)
    print("H_q is:", H_q)

    Hlijst = []
    for amino in match:
        if match[amino] == "H":
            #print(amino, ":" , match[amino])
            Hlijst.append(amino)
    print("\nHlijst is:", Hlijst)

    print("\nPositie: Amino-C")
    C_q = Queue()
    for amino in match:
        if match[amino] == "C":
            print(amino, ":" , match[amino])
            C_q.enqueue(amino)
    print("C_q is:", C_q)

    Clijst = []
    for amino in match:
        if match[amino] == "C":
            print(amino, ":" , match[amino])
            Clijst.append(amino)
    print("\nClijst is:", Clijst)

    for i in range(H_q.size()):
        current_H = H_q.dequeue()
        print("\nCurrentH is:", current_H)
        for j in range(i+2, len(Hlijst)):
            next_H = Hlijst[j]
            print("NextH is:", next_H)
            print("Predecessor is:", predecessors[next_H])
            if current_H[0] == next_H[0] and (current_H[1] == next_H[1] - 1 or current_H[1] == next_H[1] +1) and predecessors[next_H] != current_H:
                print("Predecessor is:", predecessors[next_H])
                print("NextH_hor is:", next_H)
                scoreH += 1
            elif current_H[1] == next_H[1] and (current_H[0] == next_H[0] - 1 or current_H[0] == next_H[0] +1) and predecessors[next_H] != current_H:
                print("NextH_vert is:", next_H)
                scoreH += 1
        print("ScoreH is:", scoreH)

    for i in range(C_q.size()):
        current_C = C_q.dequeue()
        print("CurrentC is:", current_C)
        for j in range(i+2, len(Clijst)):
            next_C = Clijst[j]
            print("NextC is:", next_C)
            print("Predecessor is:", predecessors[next_C])
            if current_C[0] == next_C[0] and (current_C[1] == next_C[1] - 1 or current_C[1] == next_C[1] +1) and predecessors[next_C] != current_C:
                print("Predecessor is:", predecessors[next_C])
                print("NextC_hor is:", next_C)
                scoreC += 5
            elif current_C[1] == next_C[1] and (current_C[0] == next_C[0] - 1 or current_C[0] == next_C[0] +1) and predecessors[next_C] != current_C:
                print("NextC_vert is:", next_C)
                scoreC += 5
        print("ScoreC is:", scoreC)
    
    print("\nRepresentatie:")
    for row in graph:
         print(row)

    # print("\nAmino_posities:")
    # print(amino_path)

    print("\nPosition: Predecessor")
    for pos in predecessors:
        print(pos, ":" , predecessors[pos])

    # print("\nPositie: Amino")
    # for amino in match:
    #     print(amino, ":" , match[amino])
 
    print("\nCurrPos: Richting")
    for pos in directions:
        print(pos, ":" , directions[pos])

    print("\nCurrAmi: Richting")
    for tupler in range(len(directions2)):
        print(directions2[tupler][0], ":", directions2[tupler][1])
    

if __name__ == "__main__":
    main()
