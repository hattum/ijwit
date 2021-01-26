offsets = {
    "1": [0, 1],
    "-1": [0, -1],
    "2": [-1, 0],
    "-2": [1, 0]
}

coords = [('H1', (0, 0)), ('H2', (-1, 0)), ('P3', (-1, 1)), ('H4', (0, 1)), ('H5', (1, 1)), ('H6', (2, 1)), ('P7', (2, 0)), ('H8', (1, 0))]


def directions(coords):
    dict = {}
    for i in range(len(coords) - 1):
        for direction in offsets:
            if coords[i+1][1] == (coords[i][1][0] + offsets[direction][0], 
                        coords[i][1][1] + offsets[direction][1]):
                dict[coords[i][0]] = direction
    dict[coords[-1][0]] = "0"
    return dict

print("Directions are:", directions(coords))

    