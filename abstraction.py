from CRUD_Operations import Marketoperations

class MarketCampaign:
    def __init__(self):
        self.market_operations = Marketoperations()

    def create_campaign(self):
        self.market_operations.create_campaign()

    def read_campaign(self):
        self.market_operations.read_campaign()

    def update_campaign(self):
        self.market_operations.update_campaign()

    def delete_campaign(self):
        self.market_operations.delete_campaign()

