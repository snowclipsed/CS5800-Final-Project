from graph import ALGraph

class Player:
    def __init__(self):
        self.traversed = {} #ID:NodeObject
        self.inventory = {"apples":0, "oranges":0} #oranges:orangeweight,apple:appleweight
        self.weight = self.inventory["apples"] + self.inventory["oranges"]
        self.wallet = 0
        

    def travel(self,graph:ALGraph, ID):
        graph.nodes[ID].orangestock

        # print(graph.nodes[index])
        #for key in graph.nodes[index].neighbors.keys():

    def get_weight(self):
        return self.weight
    
    def get_wallet(self):
        return self.wallet
    
    def get_inventory(self):
        return self.inventory["apples"],self.inventory["oranges"]
    
    def display_inventory(self):
        print("The current number of apples in the bag are: ", self.inventory["apples"], 
              "\nThe current number of oranges in the inventory are: ", self.inventory["oranges"],
              "\n The current weight of the bag is: ", self.weight)

    def change_inventory(self,changeapple, changeorange):
        self.inventory["apples"] += changeapple
        self.inventory["orange"] += changeorange
        return self.changeinventory["apples"], self.changeinventory["oranges"]


    def change_wallet(self,moneyvalue):
        if(self.wallet + moneyvalue > 0):
            self.wallet += moneyvalue
        else:
            print("Player has no money in the wallet. Cannot subtract money.")
        return self.wallet
    

            
