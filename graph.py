class Node:
    def __init__(self, id, name, type):
        self.vertex = id
        self.name = name
        self.placetype = type
        self.next = None

        print("Added Node " + str(self.vertex) + "of type" + str(self.placetype))


class Graph:
    def __init__(self, num):
        self.size = num
        self.graph = [None] * self.size

    # Add edges
    def add_edge(self, source, destination):
        
        s = source.vertex
        d = destination.vertex

        destination.next = self.graph[s]
        self.graph[s] = destination

        source.next = self.graph[d]
        self.graph[d] = source

    # Print the graph
    def print_agraph(self):
        for i in range(self.size):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


