#clase padre
from abc import ABCMeta, abstractmethod

class Instrumento(metaclass=ABCMeta):
    @abstractmethod
    def afinar(self):
        pass
    @abstractmethod
    def tocar(self, nota = None):
        pass
    @abstractmethod
    def tocarNota(self, nota):
        pass