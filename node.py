from collections import defaultdict
class Node:

    attribs = [
            "ID",
            "Neighbors and Weights",
            "Place Name",
            "Orange Market Stock",
            "Orange Market Price",
            "Apple Market Stock",
            "Apple Market Price"
        ]
    
    def __init__(self, id:int, name:str, orangestock:int, orangeprice:int, applestock:int, appleprice:int):
        self.id= id
        self.neighbors = defaultdict(list)
        self.name = name
        self.orangestock = orangestock
        self.orangeprice = orangeprice
        self.applestock = applestock
        self.appleprice = appleprice

        print("Created Node with ID: " + str(self.id) + " named " + self.name + " with an orange stock and price of " + str(self.orangestock) + "," + str(self.orangeprice) + " with an apple stock and price of " + str(self.applestock) + "," + str(self.appleprice))
