###########################################
## Jogador.py
##
## Created by Renan A. Pacheco  
##      Date: 25/12/2021
## 
##
###########################################

class Jogador:
    '''Jogador class para armazernar informacoes do jogador'''

    def __init__(self, nome, cor) -> None:
        self.nome = nome
        self.Cor = cor
        self.territorios = []
        self.cartas = []

# GET    
    def get_nome(self):
        return self.nome
    
    def get_cor(self):
        return self.Cor
    
    def get_territorios(self):
        return self.territorios
    
    def get_num_territorios(self):
        return len(self.territorios)
    
    def add_territorio(self, territorio):
        self.territorios.append(territorio)
    
    def del_territorio(self, territorio):
        self.territorios.remove(territorio)
