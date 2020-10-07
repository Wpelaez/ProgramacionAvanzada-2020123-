#clase Bajo
from Instrumento import Instrumento
class Bajo(Instrumento):

    def tocar(self):
        print ("Tocando Bajo")
    def afinar(self):
        print("Afinando Bajo")
    def tocarNota(self, nota):
        print("Tocando Bajo en Nota {}".format(nota))