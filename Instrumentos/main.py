from Instrumento import Instrumento

from Banda import Banda
import random

b = Banda()

b.agregarMusico("Juan")
b.agregarMusico("Maria")
b.agregarMusico("Miguel")

b.presentarBanda()


"""
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
"""