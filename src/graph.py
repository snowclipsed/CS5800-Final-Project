import pandas as pd
from node import Node
from collections import defaultdict
from pyvis.network import Network


class ALGraph:
    """
This class represents an adjacency list graph.

Attributes:
    nodes (dict): A dictionary containing the nodes of the graph.

Methods:
    add_node: Adds a single node to the graph.
    add_nodelist: Adds a list of nodes to the graph.
    display_dict: Displays the raw dictionary of nodes.
    display_nodes: Displays the nodes in the graph.
    add_edge: Adds an edge between two nodes with a specified weight.
    display_graph: Displays the graph with node details and neighbors.
    to_dataframe: Converts the graph to a pandas DataFrame.
    """
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, source):
        """
        Adds a single node to the graph.
        
        Args:
            source (Node): The node to be added to the graph.
        
        Returns:
            None
        """
        if source not in self.nodes:
            self.nodes[source.id] = source



    def add_nodelist(self, sourcelist:list):
        """
        Adds a single node to the graph.
        
        Args:
            source (Node): The node to be added to the graph.
        
        Returns:
            None
        
        Raises:
            KeyError: If the node already exists in the graph.
        
        Examples:
            To add a node with ID 1 and name "Example", use:
            |   add_node(Node(1, "Example", False))
        """
        print("\n")
        for source in sourcelist:
            if source not in self.nodes:
                self.nodes[source.id] = source
                print("Added Node with ID ", source.id, "to the graph.")
            else:
                print("Node with ID : ", source.id, " Place: ", source.name, "already exists in the graph.")
        print("\n")
                
    def display_dict(self):
        """
        Displays the raw dictionary content as key value pairs. 
        Use for debugging purposes. 
        """
        print("Raw dictionary is : \n")
        print(self.nodes)

    def return_graph(self):
        return self.nodes

    def display_nodes(self):
        """
        Display nodes in the graph.

        This method iterates through the nodes in the graph and prints their IDs and names. 
        It is used for displaying the nodes in the graph for debugging and visualization purposes.

        Args:
            self (ALGraph): The graph object.

        Returns:
            None

        Examples:
            To display the nodes in the graph, use:
            |   graph.display_nodes()

        """
        print("Displaying nodes.... \n")
        for i in self.nodes:
            print("ID: ", i, "| Name:", self.nodes[i].name)
        print("\n")
        

    def add_edge(self, source_id, destination_id, weight, p_hitch):
        """
    Adds an edge between two nodes in the graph with a specified weight.
    
    This method adds an edge between two nodes in the graph, with the specified weight. 
    It updates the neighbors dictionary of both nodes to include the other node and the weight of the edge.
    
    Args:
        source_id (int): The ID of the source node.
        destination_id (int): The ID of the destination node.
        weight (int): The weight of the edge between the source and destination nodes.
    
    Returns:
        None
    
    Examples:
        To add an edge between nodes with IDs 1 and 2 with weight 100, use:
        |   graph.add_edge(1, 2, 100)
        """
        self.nodes[source_id].neighbors[destination_id] = [weight,p_hitch]
        self.nodes[destination_id].neighbors[source_id] = [weight,p_hitch]
        print("Added edge between", source_id, " and ", destination_id, "with weight ", weight, "and with hitchhiking probability of ", p_hitch)
    

    def display_graph(self):
        """
        Display detailed information about the graph.

        This method iterates through the nodes in the graph and prints detailed information about each node, including its ID, name, neighbors, and place type. 
        It is used for displaying comprehensive details about the graph for analysis and debugging purposes.

        Args:
            self (ALGraph): The graph object.

        Returns:
            None

        Examples:
            To display detailed information about the graph, use:
            |   graph.display_graph_details()

        """
        print("Displaying graph.... \n")
        for node, properties in self.nodes.items():
            neighbors = properties.neighbors
            name = properties.name
            orangestock = properties.orangestock
            orangeprice = properties.orangeprice
            applestock = properties.applestock
            appleprice = properties.appleprice


            print("Node ID : ", node , "| Name : ",  name , "| Neighbors : " , neighbors , "| Orange Stock: ", orangestock, "| Current Market Rate of Oranges", orangeprice , "| Apples Stock: ", applestock, "| Current Market Rate of Apples", appleprice)
            print("\n")
        print("\n")



    def to_dataframe(self):
        """
        Converts the graph to a pandas DataFrame.
        
        This method iterates through the nodes in the graph and creates a pandas DataFrame with detailed information about each node, including its ID, name, neighbors, and place type. 
        It initializes an empty dictionary to store the data and then creates a DataFrame using the pandas library. It iterates through each node, extracting its properties, and appends the data to the DataFrame. Finally, it sets the display options to show all rows and columns and prints the DataFrame.
        
        Args:
            self (ALGraph): The graph object.
        
        Returns:
            dataframe (pd.DataFrame): A pandas DataFrame containing detailed information about each node in the graph.
        
        Examples:
            To convert the graph to a pandas DataFrame, use:
            |   graph.to_dataframe()
        """
        data = {}
        dataframe = pd.DataFrame(data, columns=Node.attribs)

        for node, properties in self.nodes.items():
            neighbors = properties.neighbors
            name = properties.name
            orangestock = properties.orangestock
            orangeprice = properties.orangeprice
            applestock = properties.applestock
            appleprice = properties.appleprice
            data = {"ID" : node, "Neighbors and Weights": neighbors, "Place Name": name, "Orange Market Stock": orangestock, "Orange Market Price": orangeprice, "Apple Market Stock": applestock, "Apple Market Price":appleprice}
            dataframe = pd.concat([dataframe, pd.DataFrame([data])], ignore_index=True)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        print("Converting to dataframe....")
        print(dataframe)
        print("\n")
        return dataframe
    
    def vis_graph(self):
        """
        This method uses the pyvis library to display an interactive graph of nodes in an HTML file. 
        It first initializes a Network object from the pyvis library. Then, it iterates through the nodes 
        in the graph and adds them to the network object using their IDs and labels. After that, it iterates 
        through the adjacency list to identify edges and their weights, and adds them to the network object. 
        Finally, it calls the show method of the network object to generate an HTML file with an interactive 
        visualization of the graph. This method provides a visual representation of the graph's nodes and 
        edges, allowing for interactive exploration and analysis of the graph structure.

        Returns:
            None
        """
        net = Network()

        for i in self.nodes:
            ID = i
            label = self.nodes[i].name
            net.add_node(ID, label = label)


        for i in self.nodes:
            for j in self.nodes[i].neighbors:
                net.add_edge(i, j, weight = self.nodes[i].neighbors[j][0], title = self.nodes[i].neighbors[j][1], label = str(self.nodes[i].neighbors[j][0]))

        net.set_options("""
        var options = {
          "nodes": {
            "shape": "circle",
            "size": 30
          },
          "edges": {
            "color": {
              "inherit": true
            },
            "smooth": {
              "type": "continuous"
            }
          },
          "physics": {
            "barnesHut": {
              "gravitationalConstant": -3000,
              "springConstant": 0.04,
              "springLength": 400
            },
            "minVelocity": 0.75
          }
        }
        """)

        net.show("graph_AL.html", notebook = False)





    
        
class AMGraph:
    """
        This class represents an adjacency matrix graph.
        
        It contains methods for initializing the graph, adding nodes, adding a list of nodes, and adding edges between nodes.
    """
    def __init__(self, size):
        self.nodes = {}
        self.adj_matrix = []
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size

    def add_node(self, source):
        """
        Adds a single node to the graph.
        
        Args:
            source (Node): The node to be added to the graph.
        
        Returns:
            None
        """
        if source not in self.nodes:
            self.nodes[source.id] = source


    def add_nodelist(self, sourcelist:list):
        """
        Adds a single node to the graph.
        
        Args:
            source (Node): The node to be added to the graph.
        
        Returns:
            None
        
        Raises:
            KeyError: If the node already exists in the graph.
        
        Examples:
            To add a node with ID 1 and name "Example", use:
            |   add_node(Node(1, "Example", False))
        """
        print("\n")
        for source in sourcelist:
            if source not in self.nodes:
                self.nodes[source.id] = source
                print("Added Node with ID ", source.id, "to the graph.")
            else:
                print("Node with ID : ", source.id, " Place: ", source.name, "already exists in the graph.")
        print("\n")



    def add_edge(self, source, destination, weight=None):
        """
        Displays all the nodes in the graph.
        
        Returns:
            None
        """
        if source != destination:

            self.adj_matrix[source][destination] = weight
            self.adj_matrix[destination][source] = weight

            print("Added edge between", source, " and ", destination, "with weight ", weight)
        else:
            print("Cannot extend an edge to self. Provide distinct source and destination.")

    def display_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)




    def vis_graph(self):
        """
        This method uses the pyvis library to display an interactive graph of nodes in an HTML file. 
        It first initializes a Network object from the pyvis library. Then, it iterates through the nodes 
        in the graph and adds them to the network object using their IDs and labels. After that, it iterates 
        through the adjacency matrix to identify edges and their weights, and adds them to the network object. 
        Finally, it calls the show method of the network object to generate an HTML file with an interactive 
        visualization of the graph. This method provides a visual representation of the graph's nodes and 
        edges, allowing for interactive exploration and analysis of the graph structure.

        Returns:
            None
        """
        
        net = Network()

        for i in self.nodes:
            ID = i
            label = self.nodes[i].name
            net.add_node(ID, label = label)

        for i, row in enumerate(self.adj_matrix):
            for j, element in enumerate(row):
                if element > 0:
                    net.add_edge(i, j, weight = element, label = str(element))
        net.set_options("""
        var options = {
          "nodes": {
            "shape": "circle",
            "size": 30
          },
          "edges": {
            "color": {
              "inherit": true
            },
            "smooth": {
              "type": "continuous"
            }
          },
          "physics": {
            "barnesHut": {
              "gravitationalConstant": -3000,
              "springConstant": 0.001,
              "springLength": 500
            },
            "minVelocity": 0.75
          }
        }
        """)

        net.show("graph_AM.html", notebook = False)