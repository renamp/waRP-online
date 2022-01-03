###########################################
## Territory.py
##
## Created by Renan A. Pacheco  
##      Date: 25/12/2021
## 
##
###########################################

from enum import Enum


class Continent(Enum):
    america_do_norte    = 1,
    europa              = 2,
    asia                = 3,
    america_do_sul      = 4,
    africa              = 5,
    oceania             = 6


class Territory:
    '''Territory class - store: Name, Color, Army and Symbol'''

    last_symbol  = 0
    MAX_SYMBOLS = 3

    def __init__(self, name, continent:Continent, color = 0, army = 1, symbol = 0) -> None:
        self.name = name
        self.color = color
        self.army = army
        self.borders = []
        self.continent = continent

        if symbol == 0:
            self.symbol = Territory.last_symbol + 1
            if Territory.last_symbol == Territory.MAX_SYMBOLS - 1:
                Territory.last_symbol = 0
            else:
                Territory.last_symbol += 1

# GET
    def get_name(self) -> str:
        return self.name

    def get_army(self) -> int:
        return self.army

    def get_color(self):
        return self.color

    def get_symbol(self):
        return self.symbol

    def get_borders(self):
        return self.borders

# MODIFIE
    def add_army(self, num_army) -> None:
        self.army += num_army
    
    def add_border(self, territory) -> None:
        self.borders.append(territory)
    
    def del_army(self, num_army) -> None:
        self.army -= num_army

    def set_color(self, Cor) -> None:
        self.color = Cor

    def print(self) -> None:
        text = self.name + ', Cor=' + str(self.color) + ', Exercitos=' + str(self.army)
        text += ', Simbolo=' + str(self.symbol)
        print( text )
