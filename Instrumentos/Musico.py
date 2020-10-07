from Persona import Persona
from Instrumento import Instrumento

class Musico(Persona):

    def tocar(self, Instrumento_a):
        Instrumento_a.afinar()
        Instrumento_a.tocar()
        Instrumento_a.tocarNota("Do")