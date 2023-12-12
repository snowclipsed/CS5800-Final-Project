from graph import AMGraph
from node import Node

if __name__ == "__main__":
    
    vertices = 10
    

    """
    This a list containing Node objects that represent all the places on the
    
    Rules:
    - Each place must have a unique ID at the 0th index
    - Each ID must be a whole number, starting from 0 to (vertices-1) at the end
    - Since we are storing items in a key value pair, the IDs can also be anything else but these rules are for the sake of simplicity.
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
        Node(3, "Roux Institute",  False),
        Node(4, "Old Port District", True),
        Node(5, "Portland Museum of Art", True),
        Node(6, "Eastern Promenade", True),
        Node(7, "Fore Street", False),
        Node(8, "Portland Observatory", True),
        Node(9, "Allagash Brewing Company", False)
    ]

    graph = AMGraph(10)
    graph.add_node(places[0])
    graph.add_node(places[1])
    
    graph.add_nodelist(places)
    
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 20)
    graph.add_edge(0, 3, 30)
    graph.add_edge(0, 4, 40)
    graph.add_edge(0, 5, 50)
    graph.add_edge(0, 6, 60)
    graph.add_edge(0, 7, 70)
    graph.add_edge(0, 8, 80)
    graph.add_edge(0, 9, 90)
    graph.add_edge(4, 8, 59)
    graph.add_edge(2, 7, 29)
    graph.add_edge(4, 9, 13)
    graph.add_edge(3, 7, 90)
    graph.add_edge(2, 5, 65)
    graph.add_edge(2, 3, 20)
    graph.add_edge(0, 3, 33)
    graph.add_edge(0, 5, 73)
    graph.add_edge(0, 7, 42)
    graph.add_edge(1, 5, 49)
    graph.add_edge(6, 9, 27)
    graph.add_edge(0, 4, 85)
    graph.add_edge(5, 6, 76)
    graph.add_edge(1, 4, 54)
    graph.add_edge(7, 9, 11)
    graph.add_edge(1, 8, 41)
    graph.add_edge(0, 6, 62)
    graph.add_edge(3, 8, 68)
    graph.add_edge(3, 4, 99)
    graph.add_edge(1, 6, 31)
    graph.add_edge(2, 8, 14)
    graph.add_edge(1, 3, 97)
    graph.add_edge(2, 4, 38)
    graph.add_edge(5, 7, 55)
    graph.add_edge(3, 9, 75)
    graph.add_edge(0, 1, 12)
    graph.add_edge(2, 9, 83)
    graph.add_edge(6, 8, 22)
    graph.add_edge(4, 5, 64)
    graph.add_edge(0, 2, 28)
    graph.add_edge(1, 2, 93)
    graph.add_edge(6, 7, 40)
    graph.add_edge(7, 8, 98)

    
    print("\n")

    # graph.display_nodes()
    graph.display_graph()
    graph.vis_graph()
    # graph.to_dataframe()
    # graph.display_dict()







