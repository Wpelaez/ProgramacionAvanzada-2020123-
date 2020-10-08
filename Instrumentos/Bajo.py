#clase Bajo
from Instrumento import Instrumento

class Bajo(Instrumento):

    def tocar(self, nota = None):
        if(nota==None):
            print ("Tocando Bajo")
        else:
            print("Tocando Bajo en Nota {}".format(nota))
    def afinar(self):
        print("Afinando Bajo")
    def tocarNota(self, nota):
        print("Tocando Bajo en Nota {}".format(nota))