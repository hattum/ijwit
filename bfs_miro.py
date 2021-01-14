import copy
from helpers_miro import offsets
from queue_miro import Queue, Stack

def bfs_bas(start, depth):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}
    while not queue.is_empty():
        state = queue.dequeue()
        print("State is:", state)
        if len(state) < depth:
            for direction in ["U","R", "D", "L"]:
                child = copy.deepcopy(state)
                child += direction
                queue.enqueue(child)


def bfs_miro(start, depth):
    #queue = Stack()
    queue = Queue()
    direction = "2"
    neighbour_pos = (start[0] + offsets[direction][0], 
                    start[1] + offsets[direction][1])
    queue.enqueue([start,neighbour_pos])
    paths = []
    predecessors = {start: None, neighbour_pos: start}

    while not queue.is_empty():
        state = queue.dequeue()
        print("State is:", state)
        if len(state) < depth:
            for direction in ["2", "1", "-2", "-1"]:
                print("StateHead is:", state[-1])
                neighbour_pos = (state[-1][0] + offsets[direction][0], 
                    state[-1][1] + offsets[direction][1])
                child = copy.deepcopy(state)
                print("Neighbour:", neighbour_pos)
                # child += [neighbour_pos]
                print("State[-1] is:", state[-1])
                if neighbour_pos not in child and child not in paths:
                # if neighbour_pos not in predecessors and child not in paths: #or predecessors[neighbour_pos] != (-2,0):
                    child += [neighbour_pos]
                    queue.enqueue(child)
                    print("Neighbour_pos:", neighbour_pos)
                    predecessors[neighbour_pos] = state[-1]
                    print("Predecessors:", predecessors)

                    if len(child) == depth:
                        paths.append(child)
                # if neighbour_pos in predecessors and child not in paths:
                #     if predecessors[neighbour_pos] == (-2,0): 
                # #     # and predecessors[state[-1]] == predecessors[predecessors[neighbour_pos]]: # and child not in paths: #nieuw en alles hierin ook
                # #         print("predecessors[neighbour_pos] is:", predecessors[neighbour_pos]) #nieuw
                #         queue.enqueue(child)
                #         print("Neighbour_pos2:", neighbour_pos)
                #         predecessors[neighbour_pos] = state[-1]
                #         print("Predecessors2:", predecessors)
                #         print("predecessors[neighbour_pos]2 is:", predecessors[neighbour_pos])

                #     if len(child) == depth:
                #         paths.append(child)

    print(f"\nPaths with depth{depth} are:", paths)
    print("\nLengthPaths is:", len(paths))

# def bfs(maze, start, goal):
#     queue = Queue()
#     queue.enqueue(start)
#     predecessors = {start: None}

#     while not queue.is_empty():
#         current_cell = queue.dequeue()
#         if current_cell == goal:
#             return get_path(predecessors, start, goal)
#         for direction in ["up", "right", "down", "left"]:
#             row_offset, col_offset = offsets[direction]
#             neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
#             if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
#                 queue.enqueue(neighbour)
#                 predecessors[neighbour] = current_cell
#     return None

def main():

    # start = ""
    # print(bfs_bas(start, 3))
    start = (0,0)
    print(bfs_miro(start, 4))


    # # Test 1
    # maze = [[0] * 3 for row in range(3)]
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = bfs(maze, start_pos, goal_pos)
    # assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # # Test 2
    # maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = bfs(maze, start_pos, goal_pos)
    # assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # # Test 3
    # maze = read_maze("mazes/mini_maze_bfs.txt")
    # start_pos = (0, 0)
    # goal_pos = (3, 3)
    # result = bfs(maze, start_pos, goal_pos)
    # assert result is None
if __name__ == "__main__":
    main()
    