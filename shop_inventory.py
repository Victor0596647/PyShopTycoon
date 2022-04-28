from rich import print
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

class Shop_Inv:
    def __init__(self):
        self.inven = []
        
    def addItem(self,name,type,amount):
        isFound = False
        if len(self.inven) > 0:
            for assoc in self.inven:
                if assoc[0] == str(name) and assoc[1] == str(type):
                    assoc[2] = assoc[2] + int(amount)
                    isFound = True
            if not isFound:
                self.inven.append([str(name),str(type),int(amount)])
        else:
            self.inven.append([str(name),str(type),int(amount)])
        
    def removeItem(self,index):
        self.inven.pop(int(index-1))
        
    def displayItems(self):
        #Inventory table
        invtable = Table(title="Inventory")
        invtable.add_column("#", justify="left",style="green", no_wrap=True)
        invtable.add_column("Item Name", justify="left",style="white",min_width=25)
        invtable.add_column("Item Type", justify="left",style="cyan",min_width=20)
        invtable.add_column("Item Quantity", justify="left",style="green", no_wrap=True)

        indx = 0
        for data in self.inven:
            invtable.add_row(str(indx+1),data[0],data[1],str(data[2]))
            indx+=1
            
        Console().print(invtable)