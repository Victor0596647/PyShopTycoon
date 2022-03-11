class Player:
    def __init__(self):
        # Variables
        self.__player_name = ''
        self.__player_market = ['']
        self.__player_cash = 0
        self.__player_company = ''

    def create_player(self, name, company, cash):
        self.__player_name = name
        self.__player_company = company
        self.__player_cash = cash

    def create_market(self, market_name):
        self.__player_market[0] = market_name

    # Getters
    def get_player_name(self):
        return self.__player_name
