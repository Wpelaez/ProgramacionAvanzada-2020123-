#clase Violin
from Instrumento import Instrumento
class Violin(Instrumento):

    def tocar(self):
        print ("Tocando Violin")
    def afinar(self):
        print("Afinando Violin")
    def tocarNota(self, nota):
        print("Tocando Violin en Nota {}".format(nota))