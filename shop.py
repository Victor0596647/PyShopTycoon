class Shop:
    def __init__(self):
        self.__player_markets = []
        self.__player_market = []
    
    #Getters
    def get_market(self, numX ,numY):
        return self.__player_markets[int(numX)][int(numY)]
    
    # Setters
    def create_market(self, market_name, location, state):
        self.__player_market.append(market_name)
        self.__player_market.append(location)
        self.__player_market.append(state)
        self.__player_markets.append(self.__player_market)
