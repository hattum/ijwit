#from assets.helpers_miro import offsets

offsets = {          # offstes uiteindelijkverwijderen en dan iets van bovenstaande regel erin aub!
    "1": [0, 1],
    "-1": [0, -1],
    "2": [-1, 0],
    "-2": [1, 0]
}

# coords = [('H1', (0, 0)), ('H2', (-1, 0)), ('P3', (-1, 1)), ('H4', (0, 1)), ('H5', (1, 1)), ('H6', (2, 1)), ('P7', (2, 0)), ('H8', (1, 0))]
coords = [('H', (0, 0)), ('H', (-1, 0)), ('P', (-1, 1)), ('H', (0, 1)), ('H', (1, 1)), ('H', (2, 1)), ('P', (2, 0)), ('H', (1, 0))]

def directions(coords):
    lijst = []
    for i in range(len(coords) - 1):
        for direction in offsets:
            if coords[i+1][1] == (coords[i][1][0] + offsets[direction][0], 
                        coords[i][1][1] + offsets[direction][1]):
                lijst.append((coords[i][0], direction))
                # dict[coords[i][0]] = direction
    # dict[coords[-1][0]] = "0"
    lijst.append((coords[-1][0], "0"))
    return lijst

print("Directions are:", directions(coords))

def printdirections(lijst):
    for i in lijst:
        print(i[0], ',', i[1])
lijst = directions(coords)
printdirections(lijst)

def printDirections(self):
        print("\nCurrAmi: Richting")
        for tupler in range(len(self.directions2)):
            print(self.directions2[tupler][0], ",", self.directions2[tupler][1])


    