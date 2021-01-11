from protein import Protein
from amino import Amino

def main():

    protein_list = ["HHPHHHPH", "HHPHHHPHPHHHPH", "HPHPPHHPHPPHPHHPPHPH", "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP", "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"]
    
    for item in protein_list:
        name = item
        length = len(item)
        protein = Protein('item', length)




if __name__ == "__main__":
    main()
    