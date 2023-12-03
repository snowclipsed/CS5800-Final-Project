from graph import ALGraph
from node import Node

if __name__ == "__main__":
    
    vertices = 4
    

    """
    This a list containing Node objects that represent all the places on the
    
    Rules:
    - Each place must have a unique ID at the 0th index
    - Each ID must be a whole number, starting from 0 to (vertices-1) at the end
    - The ID of a given object must be 1 more than the ID of the object before it.
        Example:
            places = [
                Node(0, "Port", True),
                Node(1, "Head Light", True),
                Node(2, "Casco Bay Islands",  False),
                Node(3, "Roux Institute",  False),
            ]
    """
    places = [
    Node(0, "Port", True),
    Node(1, "Head Light", True),
    Node(2, "Casco Bay Islands",  False),
    Node(3, "Roux Institute",  False)
    ]
    '''
    
    MAKE SURE THAT THE VERTICES CREATED IN THE ORDER IN places IS THE ORDER IN WHICH YOU ARE ENTERING THE VERTICES IN THE GRAPH!!

    This is to be done so that the "ID" property is the same as the index in the adjacency list.

    '''
    # Create graph and edges
    graph = ALGraph(vertices)

    graph.add_edge(places[0], places[1], 10) # 0 and 1 added
    graph.add_edge(places[1], places[2], 20) # 2 added
    graph.add_edge(places[1], places[3], 20) # 3 added
    graph.add_edge(places[2], places[3], 50)
    graph.add_edge(places[0], places[3], 50)
    graph.print_graph()
    
    
    graph.to_dataframe()