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
        self.territory = []
        self.cards = []

# GET    
    def get_nome(self):
        return self.name
    
    def get_cor(self):
        return self.color
    
    def get_territorios(self):
        return self.territory
    
    def get_num_territorios(self):
        return len(self.territory)
    
    def add_territorio(self, territory):
        self.territory.append(territory)
    
    def del_territorio(self, territory):
        self.territory.remove(territory)
