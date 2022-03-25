import time, sys
import keyboard
from os import system
from shop import Shop

class Shop_game:
    
    def __init__(self,name, company, cash):
        self.player_name = name
        self.player_company = company
        self.player_cash = int(cash)
        self.shop_start()
    
    def shop_start(self):
        print(self.player_name)
        print(self.player_company)
        print(self.player_cash)