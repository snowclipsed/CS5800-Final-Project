class Node:

    attribs = [
            "Vertex",
            "Neighbors and Weights",
            "Place Name",
            "Type of Place",
        ]
    
    def __init__(self, id, name, type):
        self.vertex = id
        self.name = name
        self.placetype = type
        self.next = None

        print("Added Node " + str(self.vertex) + " of type " + str(self.placetype))
