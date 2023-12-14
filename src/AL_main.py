from graph import ALGraph
from node import Node
from player import Player
from knapsack import Knapsack

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

    graph = ALGraph() 
    
    graph.add_nodelist(places) #O(V)
    
    graph.add_edge(0, 1, 30, 0.1)
    graph.add_edge(0, 2, 34, 0.05)
    graph.add_edge(0, 3, 100, 0.012)
    graph.add_edge(0, 4, 20, 0.2)
    graph.add_edge(0, 5, 35, 0.07)
    graph.add_edge(0, 6, 32, 0.18)
    graph.add_edge(0, 7, 110, 0.004)
    graph.add_edge(0, 8, 75, 0.22)
    graph.add_edge(0, 9, 55, 0.17)
    
    graph.add_edge(1, 0, 30, 0.039)
    graph.add_edge(1, 2, 36, 0.18)
    graph.add_edge(1, 3, 110, 0.028)
    graph.add_edge(1, 4, 62, 0.14)
    graph.add_edge(1, 5, 65, 0.004)
    graph.add_edge(1, 6, 67, 0.16)
    graph.add_edge(1, 7, 140, 0.037)
    graph.add_edge(1, 8, 75, 0.18)
    graph.add_edge(1, 9, 70, 0.12)
    
    graph.add_edge(2, 0, 34, 0.14)
    graph.add_edge(2, 1, 36, 0.17)
    graph.add_edge(2, 3, 29, 0.223)
    graph.add_edge(2, 4, 130, 0.038)
    graph.add_edge(2, 5, 7, 0.12)
    graph.add_edge(2, 6, 48, 0.064)
    graph.add_edge(2, 7, 24, 0.18)
    graph.add_edge(2, 8, 39, 0.1)
    graph.add_edge(2, 9, 102, 0.24)
    
    graph.add_edge(3, 0, 100, 0.0036)
    graph.add_edge(3, 1, 110, 0.243)
    graph.add_edge(3, 2, 29, 0.13)
    graph.add_edge(3, 4, 14, 0.235)
    graph.add_edge(3, 5, 30, 0.22)
    graph.add_edge(3, 6, 49, 0.14)
    graph.add_edge(3, 7, 5, 0.13)
    graph.add_edge(3, 8, 160, 0.21)
    graph.add_edge(3, 9, 69, 0.05)
    
    graph.add_edge(4, 0, 20, 0.17)
    graph.add_edge(4, 1, 62, 0.24)
    graph.add_edge(4, 2, 130, 0.22)
    graph.add_edge(4, 3, 14, 0.03)
    graph.add_edge(4, 5, 27, 0.17)
    graph.add_edge(4, 6, 70, 0.23)
    graph.add_edge(4, 7, 14, 0.21)
    graph.add_edge(4, 8, 84, 0.28)
    graph.add_edge(4, 9, 92, 0.1)
    
    graph.add_edge(5, 0, 35, 0.19)
    graph.add_edge(5, 1, 65, 0.15)
    graph.add_edge(5, 2, 7, 0.098)
    graph.add_edge(5, 3, 30, 0.084)
    graph.add_edge(5, 4, 27, 0.097)
    graph.add_edge(5, 6, 21, 0.221)
    graph.add_edge(5, 7, 29, 0.05)
    graph.add_edge(5, 8, 39, 0.24)
    graph.add_edge(5, 9, 27, 0.19)
    
    graph.add_edge(6, 0, 32, 0.17)
    graph.add_edge(6, 1, 67, 0.24)
    graph.add_edge(6, 2, 48,  0.22)
    graph.add_edge(6, 3, 49, 0.03)
    graph.add_edge(6, 4, 70, 0.17)
    graph.add_edge(6, 5, 21, 0.23)
    graph.add_edge(6, 7, 18, 0.21)
    graph.add_edge(6, 8, 34, 0.28)
    graph.add_edge(6, 9, 19, 0.1)
    
    graph.add_edge(7, 0, 110, 0.1)
    graph.add_edge(7, 1, 140, 0.05)
    graph.add_edge(7, 2, 24, 0.012)
    graph.add_edge(7, 3, 5, 0.2)
    graph.add_edge(7, 4, 14, 0.07)
    graph.add_edge(7, 5, 29, 0.18)
    graph.add_edge(7, 6, 18, 0.004)
    graph.add_edge(7, 8, 145, 0.22)
    graph.add_edge(7, 9, 150, 0.17)
    
    graph.add_edge(8, 0, 75, 0.23)
    graph.add_edge(8, 1, 75, 0.01)
    graph.add_edge(8, 2, 39, 0.126)
    graph.add_edge(8, 3, 160, 0.05)
    graph.add_edge(8, 4, 84, 0.098)
    graph.add_edge(8, 5, 39, 0.23)
    graph.add_edge(8, 6, 34, 0.2)
    graph.add_edge(8, 7, 145, 0.03)
    graph.add_edge(8, 9, 6, 0.1)
    graph.add_edge(9, 0, 55, 0.02)
    graph.add_edge(9, 1, 70, 0.019)
    graph.add_edge(9, 2, 102, 0.21)
    graph.add_edge(9, 3, 69, 0.1)
    graph.add_edge(9, 4, 92, 0.08)
    graph.add_edge(9, 5, 27, 0.11)
    graph.add_edge(9, 6, 19, 0.19)
    graph.add_edge(9, 7, 150, 0.19)
    graph.add_edge(9, 8, 6, 0.14)

   #O(1)*(V^2)
    
    # print("\n")
    
    # print("\n")

    # graph.display_nodes()
    #graph.display_graph()
    #graph.display_dict()
    # graph.to_dataframe()


    graph.vis_graph() #O(V^2)

    player = Player(0,40,20) #O(1)
    
    player.setzero(graph) #O(1)

    while(len(player.traversed)<len(places) and player.cancontinue): #runs V times, so while loop is O(V)
        knapsack = Knapsack(player,graph.nodes[player.currentnode]) #O(1)
        knapsack.apply_knapsack() #O(nlogn)
        knapsack.lottery() #O(nlogn)
        knapsack.update_values(player,graph.nodes[player.currentnode]) #O(1)
        if(player.wallet>0):
            player.travel(graph)  #O(V)
        else:
            print("\n You have no funds")
            break

            # O(1)(Graph) + O(V) (addnodelist()) + O(1)(add_edge)* V^2  + O(V^2) (vis_graph()) + O(1) (Player) + O(1) (setzero()) + O(V) (while loop ) * (O(1) (knapsack class) + O(1)(update_values()) + O(nlogn)(apply_knapsack()) + O(nlogn)(lottery()) +O(V)(travel())) = O(V*nlogn)
    if(len(player.traversed) == len(places)):
        print("\nSuccessfully Traversed the Entire Graph!! Traversal Order is: ", list(player.traversed.keys()))
    else:
        print("\nRan out of money. Traversal Order is: ", list(player.traversed.keys()))
    player.display_inventory()

    graph.vis_result(player.traversed)







