#clase Guitarra
from Instrumento import Instrumento

class Guitarra(Instrumento):

    def tocar(self, nota = None):
        if(nota == None):
            print ("Tocando Guitarra")
        else:
            print("Tocando Guitarra en Nota {}".format(nota))
    def afinar(self):
        print("Afinando Guitarra")
    def tocarNota(self, nota):
        print("Tocando Guitarra en Nota {}".format(nota))