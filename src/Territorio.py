###########################################
## Territorio.py
##
## Created by Renan A. Pacheco  
##      Date: 25/12/2021
## 
##
###########################################

class Territorio:
    '''Territorio class para armazernar informacoes como Nome, Cor, Numero de Exercitos e Simbolo'''

    last_simbolo  = 0
    MAX_SIMBOLOS = 3

    def __init__(self, nome, cor, exercito=1, simbolo=0):
        self.nome = nome
        self.cor = cor
        self.exercito = exercito
        self.fronteiras = []

        if simbolo == 0:
            self.simbolo = Territorio.last_simbolo + 1
            if Territorio.last_simbolo == Territorio.MAX_SIMBOLOS - 1:
                Territorio.last_simbolo = 0
            else:
                Territorio.last_simbolo += 1

# GET
    def get_nome(self):
        return self.nome

    def get_exercitos(self):
        return self.exercito

    def get_cor(self):
        return self.cor

    def get_simbolo(self):
        return self.simbolo

    def get_fronteiras(self):
        return self.fronteiras
        
# MODIFIE
    def add_exercitos(self, num_exercito):
        self.exercito += num_exercito
    
    def add_fronteira(self, territorio):
        self.fronteiras.append(territorio)
    
    def del_exercitos(self, num_exercito):
        self.exercito -= num_exercito

    def set_cor(self, Cor):
        self.cor = Cor

    def print(self):
        text = self.nome + ', Cor=' + str(self.cor) + ', Exercitos=' + str(self.exercito)
        text += ', Simbolo=' + str(self.simbolo)
        print( text )
    