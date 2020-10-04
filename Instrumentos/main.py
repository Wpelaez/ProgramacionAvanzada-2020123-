from abc import ABCMeta, abstractmethod
import random
#clase padre

class Instrumento(metaclass=ABCMeta):
    @abstractmethod
    def afinar(self):
        pass
    @abstractmethod
    def tocar(self):
        pass
    @abstractmethod
    def tocarNota(self, nota):
        pass

#clase Guitarra
class Guitarra(Instrumento):

    def tocar(self):
        print ("Tocando Guitarra")
    def afinar(self):
        print("Afinando Guitarra")
    def tocarNota(self, nota):
        print("Tocando Guitarra en Nota {}".format(nota))
#clase Bajo
class Bajo(Instrumento):

    def tocar(self):
        print ("Tocando Bajo")
    def afinar(self):
        print("Afinando Bajo")
    def tocarNota(self, nota):
        print("Tocando Bajo en Nota {}".format(nota))
#clase Violin
class Violin(Instrumento):

    def tocar(self):
        print ("Tocando Violin")
    def afinar(self):
        print("Afinando Violin")
    def tocarNota(self, nota):
        print("Tocando Violin en Nota {}".format(nota))
#

#empiza ciclo
for i in range(4):
    #Que ejecute Un random
    aleatorio = random.randint(1,3)
    #print (aleatorio)
    #Termina ejecutar Random


    #Un swtich

    if(aleatorio==1):
        #print("Es Guitarra")
        instrumento = Guitarra()
    elif(aleatorio==2):
        #print("Es Bajo")
        instrumento = Bajo()
    elif(aleatorio==3):
        #print("Es Violin")
        instrumento = Violin()
    else:
        print("Hubo un Error")

    #Termina Switch
    #llamar los metodos de los intrumentos

    instrumento.afinar()
    instrumento.tocar()
    instrumento.tocarNota("DO")


    #Termina llamar metodos instrumentos


    #termina ciclo
