#clase Violin
from Instrumento import Instrumento

class Violin(Instrumento):

    def tocar(self, nota = None):
        if(nota == None):
            print ("Tocando Violin")
        else:
            print("Tocando Violin en Nota {}".format(nota))
    def afinar(self):
        print("Afinando Violin")
    def tocarNota(self, nota):
        print("Tocando Violin en Nota {}".format(nota))