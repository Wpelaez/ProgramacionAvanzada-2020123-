#clase Guitarra
from Instrumento import Instrumento

class Guitarra(Instrumento):

    def tocar(self):
        print ("Tocando Guitarra")
    def afinar(self):
        print("Afinando Guitarra")
    def tocarNota(self, nota):
        print("Tocando Guitarra en Nota {}".format(nota))