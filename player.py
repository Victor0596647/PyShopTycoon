class Player:
    def __init__(self):
        # Variables
        self.__player_name = 'null'
        self.__player_market = ['']
        self.__player_cash = 0
        self.__player_company = 'null'

    def create_player(self, name, company, cash):
        self.__player_name = name
        self.__player_company = company
        self.__player_cash = int(cash)

    def create_market(self, market_name):
        self.player_market.append(market_name)

    # Getters
    def get_player_name(self):
        return '{}'.format(self.__player_name)

    def get_company(self):
        return '{}'.format(self.__player_company)

    # Setters
    def set_player_name(self, name):
        self.__player_name = name

    def set_company(self, company):
        self.__player_company = company
