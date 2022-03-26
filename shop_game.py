import time, sys
import keyboard
from os import system
from shop import Shop as mark
import json

class Shop_game:
    
    def __init__(self,name, company, cash):
        self.countries = []
        self.countriesPop = []
        self.countriesStates = []
        
        self.player_name = name
        self.player_company = company
        self.player_cash = int(cash)
        self.shop_start()
    
    def shop_start(self):
        # Check json file with locations
        
        with open("data/locations.json") as f:
            locat = json.load(f)
            
        for data in locat["countries"]:
            self.countries.append(data["name"])
            self.countriesStates.append(data["states"])
            self.countriesPop.append(data["population"])
            
        print("Welcome to " + self.countries[1])
        print(self.countriesStates[1][1])
        print(self.countriesPop[1])