###########################################
## Jogador.py
##
## Created by Renan A. Pacheco  
##      Date: 25/12/2021
## 
##
###########################################

class Jogador:
    def __init__(self, Nome, Cor) -> None:
        self.Nome = Nome
        self.Cor = Cor
        self.Territorios = []

# GET    
    def GetNome(self):
        return self.Nome
    
    def GetCor(self):
        return self.Cor
    
    def GetTerritorios(self):
        return self.Territorios
    
    
    def AddTerritorio(self, Territorio):
        self.Territorios.append(Territorio)
    
    def DelTerritorio(self, Territorio):
        self.Territorios.remove(Territorio)
