import random
import numpy as np
from node import Node
from graph import ALGraph
from player import Player


class knapsack:
        def __init__(self):
            x=round(random.random(),2)
            self.Max_capacity=0
            self.current_weight=0
            self.sell_capacity=self.current_weight*x
            self.sell_price=[0,0]         # [apple,orange]
            self.distribution=[0,0]
            self.distribution_market = [0,0] # no of oranges and apples in the market
            self.money_hold=0
            print('sell capacity: ', self.sell_capacity)

        def set_values(self,player:Player, node:Node):
            self.Max_capacity = player.get_totalcapacity()
            self.current_weight = player.get_weight()
            self.sell_price = [node.get_appleprice(),node.get_orangeprice()]
            apples, oranges = player.get_inventory()
            self.distribution = [apples,oranges]
            self.distribution_market = [node.get_applestock(), node.get_orangestock()]
            self.money_hold = player.get_wallet()


        def fractional_knapsack(self,weights, cost_per_unit, capacity):
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
            profit,amount_sold_each,arg_order= self.fractional_knapsack(self.distribution,self.sell_price,self.sell_capacity)
            print(profit,amount_sold_each,arg_order)
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
            