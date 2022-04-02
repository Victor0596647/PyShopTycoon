class Shop_Inv:
    def __init__(self):
        self.inven = []
        self.items = []
    
    def addItem(self,name,type,amount):
        self.items.append(name)
        self.items.append(type)
        self.items.append(int(amount))
        self.inven.append(self.items)
        
    def removeItem(self,index):
        self.inven.pop(index)
        
    def displayItems(self):
        print(self.inven)