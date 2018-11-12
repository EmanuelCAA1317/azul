from pecasFabrica import *

class mesaAzulejos():
    def __init__(self, quantJogadores):
        if quantJogadores < 1 or quantJogadores > 4:
            return 'Impossivel o numero de jogadores'
        elif quantJogadores == 1:
            self.lista_pecasFabricas = [pecasFabrica(),pecasFabrica()]
