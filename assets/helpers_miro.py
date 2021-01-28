offsets = {
    "1": [0, 1],
    "-1": [0, -1],
    "2": [-1, 0],
    "-2": [1, 0]
}

eiwitDict = {
        '0':["HHPHHHPH", "admissable"],
        '1':["HHPHHHPHPHHHPH", "admissable"],
        '2':["HPHPPHHPHPPHPHHPPHPH", "regular"],
        '3':["PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP", "cyclebased"],
        '4':["HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "cyclebased"],
        '5':["PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP", "regular"],
        '6':["CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC", "cyclebased"],
        '7':["HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH", "cyclereducedbyfactor"],
        '8':["HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH", "cyclereducedbyfactor"]
}