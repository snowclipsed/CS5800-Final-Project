import pandas as pd
from node import Node

"""
This is the main graph class for creating an adjacency list based graph.

The graph itself is a list of linked lists, with size num equalling the number of total vertices that may exist.

"""
class ALGraph:
    def __init__(self, num):
        self.size = num
        self.graph = [None] * self.size
        self.elements = [None] * self.size
        self.count = 0

    """
    add_edge() : takes a source node, a destination node and edge weight as parameters and creates an edge in the graph between them.
    - if the nodes already exist in the graph it will directly add an edge.
    - if the node does not exist in the graph it will add the node to the graph by extending an edge to it.
    - the addition of an edge is done by adding a list data structure as an element to the linked list corresponding to a particular element.
        - the list data structure is of the format [destination, weight] which corresponds to which element the source is attached to and 
          with how much weight in the edge.
    """
    def add_edge(self, source, destination, weight):
        
        
        if(weight>=0):
            s = source.vertex
            d = destination.vertex

            destination.next = self.graph[s]
            self.graph[s] = [destination, weight]

            source.next = self.graph[d]
            self.graph[d] = [source, weight]

        else:
            print("Weight cannot be negative for edge between" + str(source) + " and " + str(destination))
        

        if source in self.elements:
            print(str(s) + " is already in the array so it is not added to the element list.")
        else:
            self.elements[self.count] = source
            self.count += 1

        if destination in self.elements:
            print(str(d) + " is already in the array so it is not added to the element list.")
        else:
            self.elements[self.count] = destination
            self.count += 1
        


    """
    print_graph() : prints the graph. iterates through the graph list and for each element, iterates through the linked list to display all the neighbors of the node and 
                    the weight of the edges that attach to those neighbors.
        - can add more attributes if necessary
    """
    def print_graph(self):
        for i in range(self.size):
            print("Vertex " + str(i) + ":", end="")
            tempnode = self.graph[i]
            temp = tempnode[0]
            print(" -> [{}".format(temp.vertex), ", Weight : ", tempnode[1], "]", end="")
            while(temp.next != None):
                tempnode = temp.next
                temp = tempnode[0]
                print(" -> [{}".format(temp.vertex), ", Weight : ", tempnode[1], "]", end="")
            print("\n")

    def to_dataframe(self):
        data = {}
        dataframe = pd.DataFrame(data, columns = Node.attribs)

        for i in range(self.size):
            neighbors = []

            tempnode = self.graph[i]
            temp = tempnode[0]
            neighbors.append(temp.vertex)
            while(temp.next!=None):
                tempnode = temp.next
                temp = tempnode[0]
                neighbors.append(temp.vertex)

            data = {"Vertex" : i, 
                    "Neighbors and Weights": neighbors,
                "Place Name": self.elements[i].name,
                "Type of Place" : self.elements[i].placetype}
            dataframe = pd.concat([dataframe, pd.DataFrame([data])], ignore_index=True)
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
        print(dataframe)