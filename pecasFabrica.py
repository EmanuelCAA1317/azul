class pecasFabrica():
    def __init__(self, azulejo1, azulejo2, azulejo3, azulejo4, coord_x, coord_y):
        self.azulejos = [azulejo1, azulejo2,azulejo3,azulejo4]
        self.coordenadas = [coord_x,coord_y]

    def __init__(self):
        self.azulejos = [None, None, None, None]
        self.coordenadas = [0,0]

p1 = pecasFabrica()
