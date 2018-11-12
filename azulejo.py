class azulejo():
    def __init__(self, cor, tamanho, coord_x, coord_y):
        self.cor = cor
        self.tamanho = tamanho
        self.coord = [coord_x, coord_y]

    def getCor(self):
        return self.cor

    def getTamanho(self):
        return self.tamanho

    def getCoord(self):
        return self.coord

    def setCor(self,cor_nova):
        self.cor = cor_nova

    def setTamanho(self,tamanho_novo):
        self.tamanho = tamanho_novo

    def setCoord(self,x,y):
        self.coord = [x,y]

    def print(self):
        return ('cor: '+ self.cor + ' tamanho: ' + str(self.tamanho) + ' coordenadas: (' + str(self.coord[0]) + ',' + str(self.coord[1]) + ')')

