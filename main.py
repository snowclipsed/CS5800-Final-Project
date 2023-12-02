from graph import Graph
from graph import Node

if __name__ == "__main__":
    
    vertices = 3

    places = [
    Node(0, "Port", True),
    Node(1, "Head Light", True),
    Node(2, "Casco Bay Islands",  False),
    ]

    # Create graph and edges
    graph = Graph(vertices)
    graph.add_edge(places[0], places[1])
    graph.add_edge(places[2], places[1])
    
    graph.print_agraph()