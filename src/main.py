###########################################
## main.py
##
## Created by Renan A. Pacheco  
##      Date: 04/01/2022
## 
##
###########################################

from Player import Player
from Board import Board
from Territory import *


players = [Player('Renan', 1), Player('Outro', 2), Player('Fulano', 3), Player('Ciclano', 4)]
bd = Board(players)

atk_territory = bd.get_territory(TerritoryName.brasil)
def_territory = bd.get_territory(TerritoryName.venezuela)
atk_territory.add_army(3)

atk_territory.print()
def_territory.print()

print( bd.attack(atk_territory, 3, def_territory) )
print( str(bd.dices_attack) + ' ' + str(bd.dices_defense))
print('')

atk_territory.print()
def_territory.print()