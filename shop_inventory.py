from rich import print
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

class Shop_Inv:
    def __init__(self):
        self.inven = []
        
    
    def addItem(self,name,type,amount):
        added_item = []
        added_item.append(str(name))
        added_item.append(str(type))
        added_item.append(int(amount))
        
        if len(self.inven) > 0:
            for assoc in self.inven:
                if assoc[0] == added_item[0] and assoc[1] == added_item[1]:
                    assoc[2] = assoc[2] + added_item[2]
                    print(assoc)
                else:
                    print("not found")
        else:    
            self.inven.append(added_item.copy())
            added_item.clear()
        
    def removeItem(self,index):
        self.inven.pop(index)
        
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
        print(self.inven)