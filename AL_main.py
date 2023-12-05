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
    Node(0, "Port", True),
    Node(1, "Head Light", True),
    Node(2, "Casco Bay Islands",  False),
    Node(3, "Roux Institute",  False)
    ]

    graph = ALGraph()
    graph.add_node(places[0])
    graph.add_node(places[1])
    
    graph.add_nodelist(places)
    
    graph.add_edge(0,1,100)
    graph.add_edge(0,2,200)
    graph.add_edge(1,3,400)
    graph.add_edge(2,3,500)
    graph.add_edge(0,3,600)
    
    print("\n")

    graph.display_nodes()
    graph.display_graph()
    graph.to_dataframe()


    graph.vis_graph()
    # graph.display_dict()







