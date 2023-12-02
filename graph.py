class Node:
    def __init__(self, id, name, type):
        self.vertex = id
        self.name = name
        self.placetype = type
        self.next = None

        print("Added Node " + str(self.vertex) + " of type " + str(self.placetype))


class Graph:
    def __init__(self, num):
        self.size = num
        self.graph = [None] * self.size

    # Add edges
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
            

    # Print the graph
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