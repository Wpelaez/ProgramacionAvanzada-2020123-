from Musico import Musico
from Guitarra import Guitarra
from Bajo import Bajo
from Violin import Violin
import random

class Banda:
    def __init__(self):
        self.musicos = []

    def agregarMusico(self, nombre_a):
        m = Musico()
        m.setNombre(nombre_a)
        self.musicos.append(m)

    def generarInstrumento(self):
        rn = random.randint(1,3)
        if (rn == 1):
            # print("Es Guitarra")
            return Guitarra()
        elif (rn == 2):
            # print("Es Bajo")
            return Bajo()
        elif (rn == 3):
            # print("Es Violin")
            return Violin()
        else:
            print("Hubo un Error")

    def presentarBanda(self):
        for i in range(len(self.musicos)):
            self.musicos[i].presentar()
            self.musicos[i].tocar(self.generarInstrumento())
