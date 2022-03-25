class Player:
    # Variables
    def __init__(self):
        self.__player_name = ''
        self.__player_cash = 0
        self.__player_company = ''
    
    def create_player(self, name, company, cash):
        self.__player_name = name
        self.__player_company = company
        self.__player_cash = int(cash)

    # Getters
    def get_player_name(self):
        return '{}'.format(self.__player_name)

    def get_company(self):
        return '{}'.format(self.__player_company)
    
    def get_cash(self):
        return '{}'.format(str(self.__player_cash))

    # Setters
    def set_player_name(self, name):
        self.__player_name = name

    def set_company(self, company):
        self.__player_company = company
        
    def set_cash(self, money):
        self.__player_cash = int(money)
