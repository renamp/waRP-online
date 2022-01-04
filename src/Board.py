###########################################
## board.py
##
## Created by Renan A. Pacheco  
##      Date: 30/12/2021
## 
##
###########################################

import random
import itertools

from Territory import *


class Board:
    def __init__(self, players: list = []) -> None:
        self.territories = []
        self.cards = []
        self.dices_attack = []
        self.dices_defense = []

        # Create Territories
        # Ex: self.territorys.append( Territory('Alaska', Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.alaska, Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.mackenzie, Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.groelandia, Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.vancouver, Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.ottawa, Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.labrador, Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.california, Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.nova_york, Continent.america_do_norte) )
        self.territories.append( Territory(TerritoryName.mexico, Continent.america_do_norte) )

        self.territories.append( Territory(TerritoryName.brasil, Continent.america_do_sul) )
        self.territories.append( Territory(TerritoryName.argentina, Continent.america_do_sul) )
        self.territories.append( Territory(TerritoryName.peru, Continent.america_do_sul) )
        self.territories.append( Territory(TerritoryName.venezuela, Continent.america_do_sul) )

        self.territories.append( Territory(TerritoryName.islandia, Continent.europa) )
        self.territories.append( Territory(TerritoryName.inglaterra, Continent.europa) )
        self.territories.append( Territory(TerritoryName.suecia, Continent.europa) )
        self.territories.append( Territory(TerritoryName.moscou, Continent.europa) )
        self.territories.append( Territory(TerritoryName.alemanha, Continent.europa) )
        self.territories.append( Territory(TerritoryName.franca, Continent.europa) )
        self.territories.append( Territory(TerritoryName.polonia, Continent.europa) )

        self.territories.append( Territory(TerritoryName.argelia, Continent.africa) )
        self.territories.append( Territory(TerritoryName.egito, Continent.africa) )
        self.territories.append( Territory(TerritoryName.sudao, Continent.africa) )
        self.territories.append( Territory(TerritoryName.congo, Continent.africa) )
        self.territories.append( Territory(TerritoryName.madagascar, Continent.africa) )
        self.territories.append( Territory(TerritoryName.africa_do_sul, Continent.africa) )

        self.territories.append( Territory(TerritoryName.siberia, Continent.asia) )
        self.territories.append( Territory(TerritoryName.vladvostok, Continent.asia) )
        self.territories.append( Territory(TerritoryName.dudinka, Continent.asia) )
        self.territories.append( Territory(TerritoryName.omsk, Continent.asia) )
        self.territories.append( Territory(TerritoryName.tchita, Continent.asia) )
        self.territories.append( Territory(TerritoryName.aral, Continent.asia) )
        self.territories.append( Territory(TerritoryName.mongolia, Continent.asia) )
        self.territories.append( Territory(TerritoryName.china, Continent.asia) )
        self.territories.append( Territory(TerritoryName.oriente_medio, Continent.asia) )
        self.territories.append( Territory(TerritoryName.india, Continent.asia) )
        self.territories.append( Territory(TerritoryName.vietna, Continent.asia) )
        self.territories.append( Territory(TerritoryName.japao, Continent.asia) )

        self.territories.append( Territory(TerritoryName.sumatra, Continent.oceania) )
        self.territories.append( Territory(TerritoryName.borneo, Continent.oceania) )
        self.territories.append( Territory(TerritoryName.nova_guine, Continent.oceania) )
        self.territories.append( Territory(TerritoryName.australia, Continent.oceania) )

        # Create Borders
        # Examples:
        # territory = self.get_territory('territory_name')
        # territory.add_border( self.get_territory('neighbor_territory_name') )
        # OR
        # territory = self.get_territory(TerritoryName.territory_name)
        # territory.add_border( self.get_territory(TerritoryName.neighbor_territory_name) )

        territory = self.get_territory(TerritoryName.alaska)
        territory.add_border( self.get_territory(TerritoryName.mackenzie) )
        territory.add_border( self.get_territory(TerritoryName.vancouver) )
        territory.add_border( self.get_territory(TerritoryName.vladvostok) )

        territory = self.get_territory(TerritoryName.mackenzie)
        territory.add_border( self.get_territory(TerritoryName.alaska) )
        territory.add_border( self.get_territory(TerritoryName.vancouver) )
        territory.add_border( self.get_territory(TerritoryName.ottawa) )
        territory.add_border( self.get_territory(TerritoryName.groelandia) )

        territory = self.get_territory(TerritoryName.groelandia)
        territory.add_border( self.get_territory(TerritoryName.mackenzie) )
        territory.add_border( self.get_territory(TerritoryName.labrador) )
        territory.add_border( self.get_territory(TerritoryName.islandia) )

        territory = self.get_territory(TerritoryName.vancouver)
        territory.add_border( self.get_territory(TerritoryName.alaska) )
        territory.add_border( self.get_territory(TerritoryName.mackenzie) )
        territory.add_border( self.get_territory(TerritoryName.ottawa) )
        territory.add_border( self.get_territory(TerritoryName.california) )

        territory = self.get_territory(TerritoryName.ottawa)
        territory.add_border( self.get_territory(TerritoryName.mackenzie) )
        territory.add_border( self.get_territory(TerritoryName.vancouver) )
        territory.add_border( self.get_territory(TerritoryName.california) )
        territory.add_border( self.get_territory(TerritoryName.nova_york) )
        territory.add_border( self.get_territory(TerritoryName.labrador) )

        territory = self.get_territory(TerritoryName.labrador)
        territory.add_border( self.get_territory(TerritoryName.groelandia) )
        territory.add_border( self.get_territory(TerritoryName.ottawa) )
        territory.add_border( self.get_territory(TerritoryName.nova_york) )

        territory = self.get_territory(TerritoryName.california)
        territory.add_border( self.get_territory(TerritoryName.vancouver) )
        territory.add_border( self.get_territory(TerritoryName.ottawa) )
        territory.add_border( self.get_territory(TerritoryName.nova_york) )
        territory.add_border( self.get_territory(TerritoryName.mexico) )

        territory = self.get_territory(TerritoryName.nova_york)
        territory.add_border( self.get_territory(TerritoryName.ottawa) )
        territory.add_border( self.get_territory(TerritoryName.labrador) )
        territory.add_border( self.get_territory(TerritoryName.california) )
        territory.add_border( self.get_territory(TerritoryName.mexico) )

        territory = self.get_territory(TerritoryName.mexico)
        territory.add_border( self.get_territory(TerritoryName.california) )
        territory.add_border( self.get_territory(TerritoryName.nova_york) )
        territory.add_border( self.get_territory(TerritoryName.venezuela) )

        territory = self.get_territory(TerritoryName.brasil)
        territory.add_border( self.get_territory(TerritoryName.venezuela) )
        territory.add_border( self.get_territory(TerritoryName.peru) )
        territory.add_border( self.get_territory(TerritoryName.argentina) )
        territory.add_border( self.get_territory(TerritoryName.argelia) )

        territory = self.get_territory(TerritoryName.argentina)
        territory.add_border( self.get_territory(TerritoryName.peru) )
        territory.add_border( self.get_territory(TerritoryName.brasil) )

        territory = self.get_territory(TerritoryName.peru)
        territory.add_border( self.get_territory(TerritoryName.venezuela) )
        territory.add_border( self.get_territory(TerritoryName.brasil) )
        territory.add_border( self.get_territory(TerritoryName.argentina) )

        territory = self.get_territory(TerritoryName.venezuela)
        territory.add_border( self.get_territory(TerritoryName.mexico) )
        territory.add_border( self.get_territory(TerritoryName.brasil) )
        territory.add_border( self.get_territory(TerritoryName.peru) )

        territory = self.get_territory(TerritoryName.islandia)
        territory.add_border( self.get_territory(TerritoryName.groelandia) )
        territory.add_border( self.get_territory(TerritoryName.inglaterra) )

        territory = self.get_territory(TerritoryName.inglaterra)
        territory.add_border( self.get_territory(TerritoryName.islandia) )
        territory.add_border( self.get_territory(TerritoryName.suecia) )
        territory.add_border( self.get_territory(TerritoryName.alemanha) )
        territory.add_border( self.get_territory(TerritoryName.franca) )

        territory = self.get_territory(TerritoryName.suecia)
        territory.add_border( self.get_territory(TerritoryName.inglaterra) )
        territory.add_border( self.get_territory(TerritoryName.moscou) )

        territory = self.get_territory(TerritoryName.moscou)
        territory.add_border( self.get_territory(TerritoryName.suecia) )
        territory.add_border( self.get_territory(TerritoryName.omsk) )
        territory.add_border( self.get_territory(TerritoryName.aral) )
        territory.add_border( self.get_territory(TerritoryName.oriente_medio) )
        territory.add_border( self.get_territory(TerritoryName.polonia) )
        territory.add_border( self.get_territory(TerritoryName.alemanha) )

        territory = self.get_territory(TerritoryName.alemanha)
        territory.add_border( self.get_territory(TerritoryName.inglaterra) )
        territory.add_border( self.get_territory(TerritoryName.moscou) )
        territory.add_border( self.get_territory(TerritoryName.polonia) )
        territory.add_border( self.get_territory(TerritoryName.franca) )

        territory = self.get_territory(TerritoryName.franca)
        territory.add_border( self.get_territory(TerritoryName.inglaterra) )
        territory.add_border( self.get_territory(TerritoryName.alemanha) )
        territory.add_border( self.get_territory(TerritoryName.polonia) )
        territory.add_border( self.get_territory(TerritoryName.egito) )

        territory = self.get_territory(TerritoryName.polonia)
        territory.add_border( self.get_territory(TerritoryName.franca) )
        territory.add_border( self.get_territory(TerritoryName.alemanha) )
        territory.add_border( self.get_territory(TerritoryName.moscou) )
        territory.add_border( self.get_territory(TerritoryName.oriente_medio) )
        territory.add_border( self.get_territory(TerritoryName.egito) )

        territory = self.get_territory(TerritoryName.argelia)
        territory.add_border( self.get_territory(TerritoryName.brasil) )
        territory.add_border( self.get_territory(TerritoryName.egito) )
        territory.add_border( self.get_territory(TerritoryName.sudao) )
        territory.add_border( self.get_territory(TerritoryName.congo) )

        territory = self.get_territory(TerritoryName.egito)
        territory.add_border( self.get_territory(TerritoryName.franca) )
        territory.add_border( self.get_territory(TerritoryName.polonia) )
        territory.add_border( self.get_territory(TerritoryName.oriente_medio) )
        territory.add_border( self.get_territory(TerritoryName.argelia) )
        territory.add_border( self.get_territory(TerritoryName.sudao) )

        territory = self.get_territory(TerritoryName.sudao)
        territory.add_border( self.get_territory(TerritoryName.argelia) )
        territory.add_border( self.get_territory(TerritoryName.egito) )
        territory.add_border( self.get_territory(TerritoryName.congo) )
        territory.add_border( self.get_territory(TerritoryName.africa_do_sul) )
        territory.add_border( self.get_territory(TerritoryName.madagascar) )

        territory = self.get_territory(TerritoryName.congo)
        territory.add_border( self.get_territory(TerritoryName.argelia) )
        territory.add_border( self.get_territory(TerritoryName.sudao) )
        territory.add_border( self.get_territory(TerritoryName.africa_do_sul) )

        territory = self.get_territory(TerritoryName.madagascar)
        territory.add_border( self.get_territory(TerritoryName.africa_do_sul) )
        territory.add_border( self.get_territory(TerritoryName.sudao) )

        territory = self.get_territory(TerritoryName.africa_do_sul)
        territory.add_border( self.get_territory(TerritoryName.congo) )
        territory.add_border( self.get_territory(TerritoryName.sudao) )
        territory.add_border( self.get_territory(TerritoryName.madagascar) )

        territory = self.get_territory(TerritoryName.siberia)
        territory.add_border( self.get_territory(TerritoryName.dudinka) )
        territory.add_border( self.get_territory(TerritoryName.tchita) )
        territory.add_border( self.get_territory(TerritoryName.vladvostok) )

        territory = self.get_territory(TerritoryName.vladvostok)
        territory.add_border( self.get_territory(TerritoryName.siberia) )
        territory.add_border( self.get_territory(TerritoryName.tchita) )
        territory.add_border( self.get_territory(TerritoryName.china) )
        territory.add_border( self.get_territory(TerritoryName.japao) )
        territory.add_border( self.get_territory(TerritoryName.alaska) )

        territory = self.get_territory(TerritoryName.dudinka)
        territory.add_border( self.get_territory(TerritoryName.omsk) )
        territory.add_border( self.get_territory(TerritoryName.siberia) )
        territory.add_border( self.get_territory(TerritoryName.tchita) )
        territory.add_border( self.get_territory(TerritoryName.mongolia) )

        territory = self.get_territory(TerritoryName.omsk)
        territory.add_border( self.get_territory(TerritoryName.moscou) )
        territory.add_border( self.get_territory(TerritoryName.aral) )
        territory.add_border( self.get_territory(TerritoryName.china) )
        territory.add_border( self.get_territory(TerritoryName.mongolia) )
        territory.add_border( self.get_territory(TerritoryName.dudinka) )

        territory = self.get_territory(TerritoryName.tchita)
        territory.add_border( self.get_territory(TerritoryName.dudinka) )
        territory.add_border( self.get_territory(TerritoryName.siberia) )
        territory.add_border( self.get_territory(TerritoryName.vladvostok) )
        territory.add_border( self.get_territory(TerritoryName.china) )
        territory.add_border( self.get_territory(TerritoryName.mongolia) )

        territory = self.get_territory(TerritoryName.aral)
        territory.add_border( self.get_territory(TerritoryName.moscou) )
        territory.add_border( self.get_territory(TerritoryName.omsk) )
        territory.add_border( self.get_territory(TerritoryName.china) )
        territory.add_border( self.get_territory(TerritoryName.india) )
        territory.add_border( self.get_territory(TerritoryName.oriente_medio) )

        territory = self.get_territory(TerritoryName.mongolia)
        territory.add_border( self.get_territory(TerritoryName.omsk) )
        territory.add_border( self.get_territory(TerritoryName.dudinka) )
        territory.add_border( self.get_territory(TerritoryName.tchita) )
        territory.add_border( self.get_territory(TerritoryName.china) )

        territory = self.get_territory(TerritoryName.china)
        territory.add_border( self.get_territory(TerritoryName.aral) )
        territory.add_border( self.get_territory(TerritoryName.omsk) )
        territory.add_border( self.get_territory(TerritoryName.mongolia) )
        territory.add_border( self.get_territory(TerritoryName.tchita) )
        territory.add_border( self.get_territory(TerritoryName.vladvostok) )
        territory.add_border( self.get_territory(TerritoryName.japao) )
        territory.add_border( self.get_territory(TerritoryName.vietna) )
        territory.add_border( self.get_territory(TerritoryName.india) )

        territory = self.get_territory(TerritoryName.oriente_medio)
        territory.add_border( self.get_territory(TerritoryName.egito) )
        territory.add_border( self.get_territory(TerritoryName.polonia) )
        territory.add_border( self.get_territory(TerritoryName.moscou) )
        territory.add_border( self.get_territory(TerritoryName.aral) )
        territory.add_border( self.get_territory(TerritoryName.india) )

        territory = self.get_territory(TerritoryName.india)
        territory.add_border( self.get_territory(TerritoryName.oriente_medio) )
        territory.add_border( self.get_territory(TerritoryName.aral) )
        territory.add_border( self.get_territory(TerritoryName.china) )
        territory.add_border( self.get_territory(TerritoryName.vietna) )
        territory.add_border( self.get_territory(TerritoryName.sumatra) )

        territory = self.get_territory(TerritoryName.vietna)
        territory.add_border( self.get_territory(TerritoryName.india) )
        territory.add_border( self.get_territory(TerritoryName.china) )
        territory.add_border( self.get_territory(TerritoryName.borneo) )

        territory = self.get_territory(TerritoryName.japao)
        territory.add_border( self.get_territory(TerritoryName.vladvostok) )
        territory.add_border( self.get_territory(TerritoryName.china) )

        territory = self.get_territory(TerritoryName.sumatra)
        territory.add_border( self.get_territory(TerritoryName.india) )
        territory.add_border( self.get_territory(TerritoryName.australia) )

        territory = self.get_territory(TerritoryName.borneo)
        territory.add_border( self.get_territory(TerritoryName.vietna) )
        territory.add_border( self.get_territory(TerritoryName.nova_guine) )
        territory.add_border( self.get_territory(TerritoryName.australia) )

        territory = self.get_territory(TerritoryName.nova_guine)
        territory.add_border( self.get_territory(TerritoryName.borneo) )
        territory.add_border( self.get_territory(TerritoryName.australia) )

        territory = self.get_territory(TerritoryName.australia)
        territory.add_border( self.get_territory(TerritoryName.sumatra) )
        territory.add_border( self.get_territory(TerritoryName.borneo) )
        territory.add_border( self.get_territory(TerritoryName.nova_guine) )

        random.shuffle(self.territories)

        # Collect territories cards
        for territory in self.territories:
            self.cards.append(territory.card)
        
        random.shuffle(self.cards)

        if len(players) > 0:
            for territory, player in zip(self.territories, itertools.cycle(players)):
                player.add_territory(territory)
                territory.set_owner(player)


    def get_territory(self, name: Union[TerritoryName, str]):
        '''Search territory by name in list'''
        return Territory.get_territory(self.territories, name)

    def attack(self, territory_attack: Territory, num_attack: int, territory_defense: Territory) -> int:
        '''Roll dices(store in self.dices_attack and self.dices_defense) and execute the attacks, 
            return (attacks_succeed, attacks_failed) '''

        self.dices_attack = Board.roll_dices(num_attack)
        self.dices_defense = Board.roll_dices_defense(territory_defense)
        player_attack = territory_attack.owner
        player_defense = territory_defense.owner

        attacks_succeed = 0
        attacks_failed = 0
        for dice_attack, dice_defense in zip(self.dices_attack, self.dices_defense):
            if dice_attack > dice_defense:
                attacks_succeed += 1
                territory_defense.army -= 1
            else:
                attacks_failed += 1
        
        if territory_defense.army > 0:
            territory_attack.army -= attacks_succeed + attacks_failed
        else:
            player_defense.remove_territory(territory_defense)
            player_attack.add_territory(territory_defense)
            territory_attack.army -= len(self.dices_attack)
            territory_defense.army = len(self.dices_attack) - attacks_failed

        return attacks_succeed, attacks_failed


    @classmethod
    def roll_dices(cls, num_dices: int):
        '''Roll dices and return lists sorted with hiest'''

        dices = []
        for i in range(num_dices):
            dices.append(random.randint(1, 6))
        dices.sort(reverse=True)
        return dices
    
    @classmethod
    def roll_dices_defense(cls, territory: Territory):
        '''Roll defense dices '''

        num_dices = territory.army
        if(num_dices > 3):
            num_dices = 3
        return cls.roll_dices(num_dices)

