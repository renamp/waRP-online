###########################################
## Territory.py
##
## Created by Renan A. Pacheco  
##      Date: 25/12/2021
##
##
###########################################

from enum import Enum
from typing import Union


class TerritoryName(Enum):
    alaska = 'Alaska'
    mackenzie = 'Mackenzie'
    groelandia = 'Groelandia'
    vancouver = 'Vancouver'
    ottawa = 'Ottawa'
    labrador = 'Labrador'
    california = 'California'
    nova_york= 'Nova York'
    mexico = 'Mexico'

    brasil = 'Brasil'
    argentina = 'Argentina'
    peru = 'Peru'
    venezuela = 'Venezuela'

    islandia = 'Islandia'
    inglaterra = 'Inglaterra'
    suecia = 'Suecia'
    moscou = 'Moscou'
    alemanha = 'Alemanha'
    franca = 'Franca'
    polonia = 'Polonia'

    argelia = 'Argelia'
    egito = 'Egito'
    sudao = 'Sudao'
    congo = 'Congo'
    madagascar = 'Madagascar'
    africa_do_sul = 'Africa do Sul'

    siberia = 'Siberia'
    vladvostok = 'Vladvostok'
    dudinka = 'Dudinka'
    omsk = 'Omsk'
    tchita = 'Tchita'
    aral = 'Aral'
    mongolia = 'Mongolia'
    china = 'China'
    oriente_medio = 'Oriente Medio'
    india = 'India'
    vietna = 'Vietna'
    japao = 'Japao'

    sumatra = 'Sumatra'
    borneo = 'Borneo'
    nova_guine = 'Nova Guine'
    australia = 'Australia'


class Continent(Enum):
    america_do_norte    = 1,
    europa              = 2,
    asia                = 3,
    america_do_sul      = 4,
    africa              = 5,
    oceania             = 6


class Card:
    '''Card class - territory card'''

    def __init__(self, name, symbol) -> None:
        self.name = name
        self.symbol = symbol


class Territory:
    '''Territory class - store: Name, Color, Army and Symbol'''

    __last_symbol  = 0
    MAX_SYMBOLS = 3

    def __init__(self, name, continent: Continent, player = 0, army = 1, symbol = 0) -> None:

        if type(name) == TerritoryName:
            name = name.value

        self.name = name
        self.owner = player
        self.army = army
        self.borders = []
        self.continent = continent
        self.symbol = Territory.__get_symbol__(symbol)
        self.card = Card(name, symbol)


    def get_name(self) -> str:
        return self.name

    def get_army(self) -> int:
        return self.army

    def get_owner(self):
        return self.owner

    def get_symbol(self):
        return self.symbol

    def get_borders(self):
        return self.borders


    def add_army(self, num_army) -> None:
        self.army += num_army
    
    def add_border(self, territory) -> None:
        self.borders.append(territory)
    
    def del_army(self, num_army) -> None:
        self.army -= num_army

    def set_owner(self, player) -> None:
        self.owner = player

    def print(self) -> None:
        text = self.name + ', Owner=' + str(self.owner.name) + ', Exercitos=' + str(self.army)
        text += ', Simbolo=' + str(self.symbol) + ', Fronteiras=' + str( len(self.borders) ) + '('
        for i in self.borders:
            text += i.name + ','
        text = text[:-1] + ')'
        print( text )
    

    @classmethod
    def get_territory(cls, territories: list, name: Union[TerritoryName, str]):
        '''Search territory by name from list'''

        if type(name) == TerritoryName:
            name = name.value
        elif type(name) == str:
            pass
        else:
            print('not a name')
            return 
        for territory in territories:
            if name == territory.name:
                return territory
        
    @classmethod
    def __get_symbol__(cls, symbol) -> int:
        ''' Generate a symbol '''

        if symbol == 0:
            symbol = cls.__last_symbol + 1
            if cls.__last_symbol == cls.MAX_SYMBOLS - 1:
                cls.__last_symbol = 0
            else:
                cls.__last_symbol += 1
        return symbol
    
