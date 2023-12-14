import random
import numpy as np
from node import Node
from graph import ALGraph
from player import Player


class Knapsack:
        
        def __init__(self, player:Player, node:Node):
            '''
            This function implements the fractional knapsack algorithm to optimize the selection of items for selling. 
            
            Args:
                weights (list): A list of integers representing the weights of the items available for sale.
                cost_per_unit (list): A list of floats representing the selling price per unit of each item.
                capacity (float): The maximum capacity of the knapsack (i.e., the maximum weight that can be sold).
            
            Returns:
                float: The total profit obtained after selling the items.
                list: A list representing the amount of each item sold.
                list: A list of indices representing the order in which the items were selected for selling.
            
            This function first calculates the ratio of cost per unit to weight for each item and then sorts the items 
            in descending order of this ratio. It then iterates through the items, selecting the entire item if it 
            can fit in the knapsack, or a fraction of the item if it cannot. The function returns the total profit 
            obtained, the amount of each item sold, and the order in which the items were selected.
            '''
            x=round(random.random(),2)
            self.currentnode = node.id
            self.Max_capacity = player.get_totalcapacity()
            self.current_weight = player.get_weight()
            self.sell_price = [node.get_appleprice(),node.get_orangeprice()]
            apples, oranges = player.get_inventory()
            self.distribution = [apples,oranges]
            self.distribution_market = [node.get_applestock(), node.get_orangestock()]
            self.money_hold = player.get_wallet()

            self.sell_capacity=self.current_weight*x
            print("Current Node is : ", self.currentnode)
            print('Sell capacity for the node is: ', self.sell_capacity)
            


        def fractional_knapsack(self,weights, cost_per_unit, capacity):
            '''
            This function implements the fractional knapsack algorithm to optimize the selection of items for selling. 
            
            Args:
                weights (list): A list of integers representing the weights of the items available for sale.
                cost_per_unit (list): A list of floats representing the selling price per unit of each item.
                capacity (float): The maximum capacity of the knapsack (i.e., the maximum weight that can be sold).
            
            Returns:
                float: The total profit obtained after selling the items.
                list: A list representing the amount of each item sold.
                list: A list of indices representing the order in which the items were selected for selling.
            
            This function first calculates the ratio of cost per unit to weight for each item and then sorts the items 
            in descending order of this ratio. It then iterates through the items, selecting the entire item if it 
            can fit in the knapsack, or a fraction of the item if it cannot. The function returns the total profit 
            obtained, the amount of each item sold, and the order in which the items were selected.
            '''
            n = len(weights)
            ratios = [(cost_per_unit[i], weights[i], cost_per_unit[i]*weights[i]) for i in range(n)]
            temp=[ratios[0][0],ratios[1][0]]
            arg_ratio= np.flip(np.argsort(temp))
            ratios.sort(reverse=True, key=lambda x: x[0])
            total_value = 0
            knapsack = [0] * n  # To store the fraction of each item included

            for i in range(n):
                if capacity >= ratios[i][1]:
                    knapsack[i] = ratios[i][1]  # Include the entire item
                    total_value += ratios[i][2]
                    capacity -= ratios[i][1]
                else:
                    # knapsack[i] = capacity / ratios[i][1]  # Include a fraction of the item
                    knapsack[i]= int(capacity)
                    # total_value += knapsack[i] * ratios[i][2]
                    total_value += knapsack[i]*ratios[i][0]
                    break  # Knapsack is full

            return total_value, knapsack, arg_ratio

        def apply_knapsack(self):
            '''
            This function applies the fractional knapsack algorithm to optimize the selection of items for selling. 
        
            It calculates the profit, the amount of each item sold, and the order in which the items were selected. 
            The profit obtained after selling is added to the player's money hold, and the current weight is updated 
            based on the amount of each item sold. Additionally, the distribution, distribution_market, and sell_price 
            are updated based on the items sold. 
            '''
            profit,amount_sold_each,arg_order= self.fractional_knapsack(self.distribution,self.sell_price,self.sell_capacity)
            print("The Profit Obtained After Selling :", profit)
            self.money_hold= self.money_hold + profit
            self.current_weight-=sum(amount_sold_each)
            count=0
            for i in arg_order:
                self.distribution[i]= self.distribution[i]-amount_sold_each[count]
                self.distribution_market[i]= self.distribution_market[i]+ amount_sold_each[count]
                self.sell_price[i] = 0.5*self.sell_price[i]
                count+=1
            # print("current_weight: ",current_weight,"Distribution: ",distribution,"Money hold: ",money_hold)
            
        #### Lottery time
        def lottery(self):
            '''
            This function simulates a lottery event where the player can buy a random amount of items based on their remaining capacity and a random number. It calculates the profit obtained from buying the items, the amount of each item bought, and the order in which the items were selected. The profit is added to the player's money hold, and the current weight is updated based on the amount of each item bought. Additionally, the distribution and distribution_market are updated based on the items bought. 
            '''
            y=round(random.random(),2)
            remmaining_capacity= self.Max_capacity- self.current_weight
            buy_capacity=remmaining_capacity*y
            profit2,amount_bought_each,arg_order=self.fractional_knapsack(self.distribution_market,self.sell_price,buy_capacity)
            count=0
            for i in arg_order:
                self.distribution[i]= self.distribution[i]+amount_bought_each[count]
                self.distribution_market[i]= self.distribution_market[i]-amount_bought_each[count]
                count+=1
            self.current_weight+=sum(amount_bought_each)
        
        def update_values(self,player:Player, node:Node):
            player.set_wallet(self.money_hold)
            player.set_inventory(self.distribution)
            node.set_appleprice(self.sell_price[0])
            node.set_orangeprice(self.sell_price[1]) # put apples and oranges inside
            node.set_applestock(self.distribution_market[0])
            node.set_orangestock(self.distribution_market[1])
            