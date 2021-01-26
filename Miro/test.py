def scoreH(coordsmatch):
    scoreH = 0
    scoreC = 0
    for i in range(len(coordsmatch)):
        current = coordsmatch[i][1]
        for j in range(i+2, len(coordsmatch)):
            next = coordsmatch[j][1]
            if current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "H" and coordsmatch[j][0] == "H":
                scoreH += -1
            elif current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "C":
                scoreC += -5
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "H" and coordsmatch[j][0] == "H":
                scoreH += -1
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "C":
                scoreC += -5
    return scoreH + scoreC

def mapper(coords, eiwit):
    coordsmatch = []
    for element in zip(coords, eiwit):
        pos = element[0]
        amino = element[1]
        coordsmatch.append((amino, pos))
    return coordsmatch

coords = [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, 1), (-3, 2), (-4, 2), (-4, 1), (-5, 1), (-6, 1), (-7, 1), (-7, 0), (-7, -1), (-6, -1), (-5, -1), (-5, 0), (-4, 0), (-4, -1), (-3, -1), (-3, -2), (-4, -2), (-5, -2), (-5, -3), (-4, -3), (-3, -3), (-3, -4), (-3, -5), (-2, -5), (-2, -4), (-2, -3), (-2, -2), (-1, -2), (-1, -1), (-2, -1)]
eiwit = "PPPHHCHHHPPPPPHHHHHHHPPHHPPPPHHPCHPP"
#eiwit = "PPPHHC"
def factor(eiwit, depth):
    count = 0
    for i in range(0, depth):
        if eiwit[i] == "H" or eiwit[i] == "C":
            count += 1
    return count/depth
fact = factor(eiwit, 6)
print(fact)
# res = mapper(coords, eiwit)
# print(res)
#print(count)