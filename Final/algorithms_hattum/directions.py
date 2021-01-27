import csv
#from assets.helpers_miro import offsets

coords = [('H', (0, 0)), ('H', (-1, 0)), ('P', (-1, 1)), ('H', (0, 1)), ('H', (1, 1)), ('H', (2, 1)), ('P', (2, 0)), ('H', (1, 0))]


offsets = {          # offsets uiteindelijk verwijderen en dan iets van bovenstaande regel erin aub!
            "1": [0, 1],
            "-1": [0, -1],
            "2": [-1, 0],
            "-2": [1, 0]
}

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

lijstig = directions(coords)

with open('Visualisation.csv', 'w', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(["Amino", "Fold"])
    for i in range(len(coords)):
        print("Amino is:", lijstig[i][0])
        print("Richting is:", lijstig[i][1])
        writer.writerow([lijstig[i][0], lijstig[i][1]])
    #writer.writerow(["Score:", self.score])
    writer.writerow(["Score:"])

