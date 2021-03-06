import time, sys
import keyboard
from os import system
from shop import Shop
import json
from rich import print
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from shop_inventory import Shop_Inv

class Shop_game:
    mark = Shop()
    inv = Shop_Inv()
    
    def __init__(self,name, company, cash):
        self.countries = []
        self.countriesPop = []
        self.countriesStates = []
        
        # Checks Json file
        with open("data/locations.json") as f:
            locat = json.load(f)
            
        for data in locat["countries"]:
            self.countries.append(data["name"])
            self.countriesStates.append(data["states"])
            self.countriesPop.append(data["population"])
        
        self.player_name = name
        self.player_company = company
        self.player_cash = int(cash)
        self.shop_start()
    
    # Displays Countries
    def dispCountries(self):
        console = Console()
        showCon = Text()
        i = 0
        for data in self.countries:
            showCon.append("\n[" + str(i+1) + "] Country: " + data + "\n   Population: " + str(self.countriesPop[i])+ "\n")
            i+=1
        console.print(Panel.fit(showCon))
        showCon = ""
        
    def dispStates(self,choice):
        console = Console()
        showCon = Text()
        i = 0
        for data in self.countriesStates[choice-1]:
            showCon.append("\n[" + str(i+1) + "] " + data + "\n")
            i+=1
        console.print(Panel.fit(showCon))
        
    def shop_start(self):
        system("CLS")
            
        self.dispCountries()
        print(Panel.fit("Choose a country to start your Market Career!"))
        while(True):
            try:
                sel = int(input("> "))
                selCountry = self.countries[sel-1]
                self.dispStates(sel)
                print(Panel.fit("Now choose a state"))
                inp = int(input("> "))
                selState = self.countriesStates[sel-1][inp-1]
                print(Panel.fit("Finally, What name would your shop be?"))
                Mname = input("> ")
                self.mark.create_market(Mname,selCountry,selState)
                break
            except Exception as err:
                print(Panel.fit(str(err),style="#B3001B",title="Error Exception"))
                time.sleep(1)
                self.shop_start()
        system("cls");
        self.game(0)
        
    def game(self,mk):
        print(Panel.fit("Shop: " + self.mark.get_market(mk,0) + "   Location: " + self.mark.get_market(mk,1) + ", " + self.mark.get_market(mk,2) + "\n"
                        + "If you need to know commands type in 'help'"))
        while(True):
            try:
                inp = input("> ")
                if inp == "cls":
                   system("CLS")
                elif inp == "help":
                    print("-help\n-cls\n-exit\n-inven\n-order\n")
                elif inp == "exit":
                    break
                elif inp == "inven":
                   self.inventory()
                elif inp == "order":
                    print("will be added soon!")
                else:
                    print(Panel("'" + str(inp) + "'",style="#B3001B",title="Input Error",width=40,title_align="left"))
            except Exception as err:
                print(Panel.fit(str(err),style="#B3001B",title="Error Exception"))
                
    def inventory(self):
        self.inv.displayItems()