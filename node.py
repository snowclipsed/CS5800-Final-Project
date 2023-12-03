from collections import defaultdict
class Node:

    attribs = [
            "ID",
            "Neighbors and Weights",
            "Place Name",
            "Type of Place",
        ]
    
    def __init__(self, id, name, type):
        self.id= id
        self.neighbors = {}
        self.name = name
        self.placetype = type

        print("Created Node " + str(self.id) + " of type " + str(self.placetype))
