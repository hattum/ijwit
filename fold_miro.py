from queue_miro_backup import Queue, AminoQueue

class Fold():
    #def __init__(self, eiwit):
    def __init__(self, eiwit, algorithm): #nieuw
        self.match = {}
        self.eiwit = eiwit
        self.amino_q = AminoQueue(eiwit)
        self.algorithm = algorithm
        self.choice()
        #self.amino_path, self.predecessors, self.directions, self.directions2 = self.amino_q.choice()
        #self.amino_path, self.predecessors, self.directions, self.directions2 = self.amino_q.cyclefold()
        #self.amino_path, self.predecessors, self.directions, self.directions2 = self.amino_q.{algorithm}() #nieuw
        self.graph = [["   " for i in range(len(eiwit))] for i in range(len(eiwit))]

        for j, element in enumerate(zip(self.amino_path, list(self.eiwit))):
            self.pos = element[0]
            self.amino = element[1]
            self.match[self.pos] = self.amino
            self.graph[self.pos[0]][self.pos[1]] = self.amino+str(j)
            #graph[pos[0]][pos[1]] = self.amino
        

    def choice(self):
        if self.algorithm == "cyclefold":
            self.amino_path, self.predecessors, self.directions, self.directions2 = self.amino_q.cyclefold()

    def plot(self):
        print("\nRepresentatie:")
        for row in self.graph:
            print(row)

    def makeH_q(self):
        print("\nPositie: Amino-H")
        H_q = Queue()
        for amino in self.match:
            if self.match[amino] == "H":
                print(amino, ":" , self.match[amino])
                H_q.enqueue(amino)
        return H_q
        #print("H_q is:", H_q)
    
    def makeH_lijst(self):
        Hlijst = []
        for amino in self.match:
            if self.match[amino] == "H":
                Hlijst.append(amino)
        return Hlijst
        #print("\nHlijst is:", Hlijst)

    def makeC_q(self):
        print("\nPositie: Amino-C")
        C_q = Queue()
        for amino in self.match:
            if self.match[amino] == "C":
                print(amino, ":" , self.match[amino])
                C_q.enqueue(amino)
        return C_q
        #print("C_q is:", C_q)
        
    def makeC_lijst(self):
        Clijst = []
        for amino in self.match:
            if self.match[amino] == "C":
                print(amino, ":" , self.match[amino])
                Clijst.append(amino)
        return Clijst
        #print("\nClijst is:", Clijst)

    def scoreH(self):
        scoreH = 0
        H_q = self.makeH_q()
        H_lijst = self.makeH_lijst()
        while not H_q.is_empty():
        #for i in range(H_q.size()):
            current_H = H_q.dequeue()
            print("\nCurrentH is:", current_H)
            for j in range(len(H_lijst)):
            #for j in range(i+2, len(H_lijst)):
                next_H = H_lijst[j]
                print("NextHlijst is:", next_H)
                print("CurrentH is:", current_H)
                #print("Predecessor is:", self.predecessors[next_H])
                if current_H[0] == next_H[0] and (current_H[1] == next_H[1] - 1 or current_H[1] == next_H[1] +1) and self.predecessors[next_H] != current_H:
                    print("NextH_hor is:", next_H)
                    print("Predecessor is:", self.predecessors[next_H])
                    scoreH += 1
                elif current_H[1] == next_H[1] and (current_H[0] == next_H[0] - 1 or current_H[0] == next_H[0] +1) and self.predecessors[next_H] != current_H:
                    print("NextH_vert is:", next_H)
                    print("Predecessor is:", self.predecessors[next_H])
                    scoreH += 1
            H_lijst.pop(0)
        return scoreH
        # print("ScoreH is:", scoreH)

    def scoreC(self):
        scoreC = 0
        C_q = self.makeC_q()
        C_lijst = self.makeC_lijst()
        for i in range(C_q.size()):
            current_C = C_q.dequeue()
            #print("CurrentC is:", current_C)
            for j in range(i+2, len(C_lijst)):
                next_C = C_lijst[j]
                #print("NextC is:", next_C)
                #print("Predecessor is:", predecessors[next_C])
                if current_C[0] == next_C[0] and (current_C[1] == next_C[1] - 1 or current_C[1] == next_C[1] +1) and self.predecessors[next_C] != current_C:
                    #print("Predecessor is:", predecessors[next_C])
                    #print("NextC_hor is:", next_C)
                    scoreC += 5
                elif current_C[1] == next_C[1] and (current_C[0] == next_C[0] - 1 or current_C[0] == next_C[0] +1) and self.predecessors[next_C] != current_C:
                    #print("NextC_vert is:", next_C)
                    scoreC += 5
            return scoreC
        #print("ScoreC is:", scoreC)

    def printDirections(self):
        print("\nCurrAmi: Richting")
        for tupler in range(len(self.directions2)):
            print(self.directions2[tupler][0], ",", self.directions2[tupler][1])

    # def scoreHvar(self):
    #     scoreHvar = 0
    #     #H_q = self.makeH_q()
    #     #H_lijst = self.makeH_lijst()
    #     while not self.amino_q.is_empty():
    #         current = self.amino_q.dequeue()
    #         print("\nCurrent is:", current)
    #         for j in range(len(self.eiwit)):
    #             next = self.eiwit[j]
    #             print("Nextstring is:", next)
    #             print("Current is:", current)
    #             #print("Predecessor is:", predecessors[next_H])
    #             if current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and self.predecessors[next] != current and current == "H" and next == "H":
    #                 #print("Predecessor is:", predecessors[next_H])
    #                 print("Next_hor is:", next)
    #                 print("Predecessor is:", self.predecessors[next])
    #                 scoreHvar += 1
    #             elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and self.predecessors[next] != current and current == "H" and next == "H":
    #                 print("Next_vert is:", next)
    #                 print("Predecessor is:", self.predecessors[next])
    #                 scoreHvar += 1
    #         return scoreHvar
    #     # print("ScoreHvar is:", scoreHvar)


