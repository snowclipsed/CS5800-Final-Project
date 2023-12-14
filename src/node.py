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
    
    def __init__(self, id:int, name:str, applestock:int, appleprice:int, orangestock:int, orangeprice:int):
        self.id= id
        self.neighbors = {}
        self.name = name
        self.orangestock = orangestock
        self.orangeprice = orangeprice
        self.applestock = applestock
        self.appleprice = appleprice
        self.visited = False

        print("Created Node with ID: " + str(self.id) + " named " + self.name + " with an orange stock and price of " + str(self.orangestock) + "," + str(self.orangeprice) + " with an apple stock and price of " + str(self.applestock) + "," + str(self.appleprice))

    def get_id(self):
        return self.id

    def get_neighbors(self):
        return self.neighbors

    def get_placename(self):
        return self.name

    def get_orangestock(self):
        return self.orangestock

    def get_orangeprice(self):
        return self.orangeprice

    def get_applestock(self):
        return self.applestock

    def get_appleprice(self):
        return self.appleprice
    
    def set_id(self, new_id:int):
        self.id = new_id
        return self.id
    
    def set_placename(self, new_name:str):
        self.name = new_name
        return self.name
    
    def set_orangestock(self, new_orangestock:int):
        self.orangestock = new_orangestock
        return self.orangestock
    
    def set_orangeprice(self, new_orangeprice:int):
        self.orangeprice = new_orangeprice
        return self.orangeprice
    
    def add_applestock(self,added_apples:int):
        self.applestock += added_apples

    def add_orangestock(self, added_oranges:int):
        self.orangestock += added_oranges
    
    def set_applestock(self, new_applestock:int):
        self.applestock = new_applestock
        return self.applestock
    
    def set_appleprice(self, new_appleprice:int):
        self.appleprice = new_appleprice
        return self.appleprice
