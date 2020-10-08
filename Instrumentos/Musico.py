from Persona import Persona

class Musico(Persona):

    def tocar(self, Instrumento_a):
        Instrumento_a.afinar()
        Instrumento_a.tocar()
        #Instrumento_a.tocarNota("Do")
        Instrumento_a.tocar("Do")