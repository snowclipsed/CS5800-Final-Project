"""
    Creating a custom node definition in order to store the following data.
        1) Name of the Location.
        2) Type of Location.
        3) Neighbors or Adjacent Locations - Using an Adjacency list.
"""
class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.neighbors = []
    
    def fetch_location_name(self):
        return self.name
    
    def fetch_location_type(self):
        return self.type

    def fetch_neighbors(self):
        return self.neighbors
    
    def add_neighbor(self, node):
        self.neighbors.append(node)
    
    def add_neighbors(self, nodes):
        self.neighbors.extend(nodes)

"""
    Creating an enum to track the type of location. 
    As of now, there are only 2 types of locations: 
        1) Dull - There is nothing to do here.
        2) Vibrant - There is a lot to do here.
"""
from enum import Enum
class LocationType(Enum):
    START = "Start"
    DULL = "Dull"
    VIBRANT = "Vibrant"

"""
    Creating a class for Graph which will instantiate and set up the graph our hitch-hiker will navigate.
"""
class Graph:
    def __init__(self):
        # Creating the start node where our hitch-hiker resides.
        self.current_node = Node("A", LocationType.START)

        # Temporary Nodes to test the concept.
        B = Node("B", LocationType.VIBRANT)
        C = Node("C", LocationType.DULL)
        D = Node("D", LocationType.VIBRANT)
        E = Node("E", LocationType.DULL)

        current.add

