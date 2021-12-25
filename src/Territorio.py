###########################################
## Territorio.py
##
## Created by Renan A. Pacheco  
##      Date: 25/12/2021
## 
##
###########################################

class Territorio:
    def __init__(self, Nome, Cor, Exercito, Simbolo) -> None:
        self.Nome = Nome
        self.Cor = Cor
        self.Exercito = Exercito
        self.Simbolo = Simbolo

# GET
    def GetNome(self):
        return self.Nome
        
    def GetExercitos(self):
        return self.Exercito

    def GetCor(self):
        return self.Cor

    def GetSimbolo(self):
        return self.Simbolo

# MODIFIE
    def AddExercitos(self, NumExercito):
        self.Exercito += NumExercito
    
    def DelExercitos(self, NumExercito):
        self.Exercito -= NumExercito

    def ChangeCor(self, Cor):
        self.Cor = Cor

    