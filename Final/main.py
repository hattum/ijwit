from classes_hattum import grid, protein

from algorithms_hattum import greedy_lookahead



if __name__ == "__main__":
    protein = protein.Protein("HHPHHHPH")
    grid = grid.Grid(protein.length)
    print(type(grid))
    algo = greedy_lookahead.Greedy_lookahead(protein,grid,5)