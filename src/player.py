from graph import ALGraph
import random as rand


class Player:
    def __init__(self, currentnode, wallet, capacity):
        self.traversed = {} #ID:NodeObject
        self.inventory = {"apples":1, "oranges":1} #oranges:orangeweight,apple:appleweight #add random later
        self.weight = self.inventory["apples"] + self.inventory["oranges"]
        self.wallet = wallet
        self.totalcapacity = capacity
        self.currentcapacity = self.totalcapacity-self.weight
        self.currentnode = currentnode
        self.cancontinue = True
    
    def setzero(self,graph:ALGraph):
        if(self.currentnode == 0):
            graph.nodes[0].visited = True
            self.traversed[0] = graph.nodes[0]

    def travel(self,graph:ALGraph):

        print("\nCurrent Node is :", self.currentnode)
        thisnode = self.currentnode
        cost_to_node = 0
        for key in graph.nodes[self.currentnode].neighbors.keys():
           if(graph.nodes[key].visited == False):
            
            if(self.hardik(graph.nodes[self.currentnode].neighbors[key][1]) == False):
                travel_cost = graph.nodes[self.currentnode].neighbors[key][0]
            else:
                travel_cost = 0
                print("Can take car to node ", key)
            potential_profit = graph.nodes[key].appleprice*self.inventory["apples"] + graph.nodes[key].orangeprice*self.inventory["oranges"]
            total_change = potential_profit - travel_cost
            if(total_change>cost_to_node and self.wallet-travel_cost>=0):
                cost_to_node = travel_cost
                self.currentnode = key
        if(self.currentnode != thisnode):
            self.wallet -= cost_to_node
            self.traversed[self.currentnode] = graph.nodes[self.currentnode]
            graph.nodes[self.currentnode].visited = True
            print("Traveled to ", self.currentnode, "\nCurrent Wallet: ", self.get_wallet(), "\n")
        else:
            print("Not enough money in wallet to continue. Current Wallet : ", self.wallet)
            self.cancontinue = False
        


    def hardik(self,probability):
        random_number = rand.random()

        car_available = random_number <= probability

        return car_available

    def get_weight(self):
        return self.weight
    
    def get_totalcapacity(self):
        return self.totalcapacity
    
    def set_capacity(self,newcapacity):
        self.totalcapacity = newcapacity

    def get_currentcapacity(self):
        return self.currentcapacity
    
    def get_wallet(self):
        return self.wallet
    
    def set_wallet(self,money):
        self.wallet = money
    
    def get_inventory(self):
        return self.inventory["apples"],self.inventory["oranges"]
    
    def display_inventory(self):
        print("The current number of apples in the bag are: ", self.inventory["apples"], 
              "\nThe current number of oranges in the inventory are: ", self.inventory["oranges"],
              "\n The current weight of the bag is: ", self.weight)

    def change_inventory(self,changeapple, changeorange):
        self.inventory["apples"] += changeapple
        self.inventory["orange"] += changeorange
        return self.inventory["apples"], self.inventory["oranges"]
    
    def set_inventory(self,newinventory):
        self.inventory["apples"] = newinventory[0]
        self.inventory["orange"] = newinventory[1]
        return self.inventory["apples"], self.inventory["oranges"]


    def change_wallet(self,moneyvalue):
        if(self.wallet + moneyvalue > 0):
            self.wallet += moneyvalue
        else:
            print("Player has no money in the wallet. Cannot subtract money.")
        return self.wallet
    

            
