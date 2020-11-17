from random import randint

class Numero():

    def generar_lista_azar(self):
        cifras = self.__numero_cifras__()
        lista = self.__asignar_numeros__(cifras)
        lista = self.__norepetir__(lista)
        return lista

    def __numero_cifras__(self):
        rango_off = True
        while rango_off:
            while True:
                cifras = input("Digite el numero de cifras de 3 a 5: ")
                if cifras.isdigit():
                    cifras = int(cifras)
                    break
                else:
                    print("DIGITE UN NUMERO!")
            if cifras > 5 or cifras < 3:
                print("Digite un numero del 3 al 5! Usted digite {}".format(cifras))
            else:
                rango_off = False
        return cifras

    def __asignar_numeros__(self, cifras):
        lista = []
        for i in range(cifras):
            (lista).append(randint(0, 9))
        return lista

    def __norepetir__(self, lista):
        i = 0
        while (i < len(lista)):
            i2 = 0
            while (i2 < len(lista)):
                if lista[i] == lista[i2] and i != i2:
                    lista[i] = randint(0, 9)
                    i2 = 0
                else:
                    i2 += 1
            i += 1
        return lista

    def generar_lista_usuario(self, cifras):
        repitio = True
        mas_cifras = True
        while (repitio) or (mas_cifras):
            while True:
                numero_usuario = input(f"Digite un numero de {cifras} cifras sin repetir cifras: ")
                if numero_usuario.isdigit():
                    break
                else:
                    print("DIGITE UN NUMERO!")
            lista_usuario = [int(x) for x in numero_usuario]
            if len(lista_usuario) != cifras:
                print("Digite un Numero de {} cifras!!".format(cifras))
                mas_cifras = True
            else:
                mas_cifras = False
            i = 0
            while (i < len(lista_usuario)):
                i2 = 0
                while (i2 < len(lista_usuario)):
                    if lista_usuario[i] == lista_usuario[i2] and i != i2:
                        print("SIN REPETIR NUMEROS!!")
                        repitio = True
                        i2 = len(lista_usuario) + 1
                        i = len(lista_usuario) + 1
                    else:
                        repitio = False
                    i2 += 1
                i += 1
        return lista_usuario