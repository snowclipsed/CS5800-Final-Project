from graph import Graph
from graph import Node

if __name__ == "__main__":
    
    vertices = 4

    places = [
    Node(0, "Port", True),
    Node(1, "Head Light", True),
    Node(2, "Casco Bay Islands",  False),
    Node(3, "Casco Bay Islands",  False),
    ]

    # Create graph and edges
    graph = Graph(vertices)
    graph.add_edge(places[0], places[1], 10)
    graph.add_edge(places[0], places[2], 20)
    graph.add_edge(places[0], places[3], 30)
    
    graph.print_graph()