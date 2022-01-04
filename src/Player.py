###########################################
## Player.py
##
## Created by Renan A. Pacheco  
##      Date: 25/12/2021
## 
##
###########################################

class Player:
    '''Player class - store player data'''

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        self.territories = []
        self.cards = []

# GET    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_territories(self):
        return self.territories
    
    def get_num_territories(self):
        return len(self.territories)
    
    def add_territory(self, territory):
        self.territories.append(territory)
        territory.owner = self
    
    def remove_territory(self, territory):
        self.territories.remove(territory)
