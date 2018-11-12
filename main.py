from azulejo import *
import random
import pecasFabrica
import tabuleiroJogador


listaAzulejos = []

for i in range(20):
    listaAzulejos.append(azulejo('blue',10,0,0))
    listaAzulejos.append(azulejo('red',10,0,0))
    listaAzulejos.append(azulejo('white',10,0,0))
    listaAzulejos.append(azulejo('black',10,0,0))
    listaAzulejos.append(azulejo('green',10,0,0))

for i in range(10):
    print(listaAzulejos[i].print())

random.shuffle(listaAzulejos)

for i in range(10):
    print(listaAzulejos[i].print())
