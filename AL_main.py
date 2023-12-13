from graph import ALGraph
from node import Node

if __name__ == "__main__":
    
    vertices = 4
    

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
        Node(0, "Portland", 12, 8, 4, 23),
        Node(1, "Westbrook", 6, 20, 11, 12),
        Node(2, "Bangor", 2, 25, 1, 23),
        Node(3, "Lewiston", 14, 5, 12, 8),
        Node(4, "Waterville", 8, 12, 9, 15),
        Node(5, "Brewer", 0, 30, 15, 4),
        Node(6, "Augusta", 14, 5, 30, 1),
        Node(7, "Auburn", 11, 10, 2, 25),
        Node(8, "Biddeford", 5, 30, 11, 9),
        Node(9, "Saco", 2, 20, 3, 18)
    ]

    # graph = ALGraph()
    # graph.add_node(places[0])
    # graph.add_node(places[1])
    
    # graph.add_nodelist(places)
    
    # graph.add_edge(0, 1, [10,0.1])
    # graph.add_edge(0, 2, 20)
    # graph.add_edge(0, 3, 30)
   
    
    # print("\n")
    
    # print("\n")

    # graph.display_nodes()
    # graph.display_graph()
    # graph.to_dataframe()


    # graph.vis_graph()
    # graph.display_dict()







