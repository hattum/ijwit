""" Program room.py consists of only one class that initializes a Room with some
members and that has a setter and some getters. It is exportable to other programms
(like adventure.py) in which a room object plays a role

by Miro Zwering with ID 12910260
"""

from collections import namedtuple

#class Room(object):
class Amino():

    # Initializes a Room
    #def __init__(self, room_id, name, description, visited = False):
    def __init__(self, amino_id, ch, i, j):

        # # Dictionary that maps directions like "EAST" to other room objects
        # self.connections = {}

        # Amino properties
        #self.visited = visited
        self.amino_id = amino_id
        self.ch = ch
        self.i = i
        self.j = j

    # Adds a given direction and the connected room to our room object.
    def add_connection(self, direction, room):
        self.connections[direction] = room

    # Checks whether the given direction has a connection from this room.
    def has_connection(self, direction):
        return direction in self.connections

    # Retrieves room connected to this room.
    def get_connection(self, direction):
        return self.connections[direction]

    # Sets value of 'visited' to True
    def set_visited(self):
        self.visited = True

    # Returns True if the room was already visited else False
    def already_visited(self):
        if self.visited:
            return True
        return False

def main():
    # create an Amino namedtuple
    Amino = namedtuple("Amino", "i j z")

    H1 = Amino(3, 3, 0)
    H2 = Amino(2, 3, 0)
    P3 = Amino(2, 4, 0)

    print(H1, H2, P3)
    print(H1.i, H2.j, P3.z)

    # use _replace to create a new instance
    H1 = H1._replace(i=100)
    print(H1)




if __name__ == "__main__":
    main()
