class Archivo():

    def __init__(self):
        self.lista_cifra = []

    def escribir(self, nombre, cifras, intentos, picas, fijas, gano):
        f = open("resultados.txt", "a")
        f.write("{},{},{},{},{},{}\n".format(nombre, cifras, intentos, picas, fijas, gano))
        f.close()

    def lider_cifras(self, cifras):
        f = open("resultados.txt", "r")
        for x in f.readlines():
            #lista_extraccion = [x1 for x1 in x.split(",")]
            lista_extraccion = x.split(",")
            lista_extraccion[1] = int(lista_extraccion[1])
            lista_extraccion[2] = int(lista_extraccion[2])
            if lista_extraccion[1] == cifras and (lista_extraccion[5])[0] == 'T':
                self.lista_cifra.append(lista_extraccion)
        f.close()

        if self.lista_cifra:
            self.lista_cifra.sort(key=lambda x: x[2])
            print("En {} Cifras el Lider es:".format(cifras))
            for lideres in self.lista_cifra:
                if lideres[2] == (self.lista_cifra[0])[2]:
                    print("{}, Intentos: {}".format(lideres[0], lideres[2]))
        else:
            print("No hay Lideres con victoria!")

    def verificar_usuario_cifras(self, nombre, cifras):
        no_juega = False
        f = open("resultados.txt", "r")
        for lineas in f.readlines():
            #lista_temp = [x for x in lineas.split(",")]
            lista_temp = lineas.split(",")
            if lista_temp[0].lower() == nombre.lower() and lista_temp[1] == str(cifras):
                no_juega = True
                print("ERROR! El usuario {}, ya tiene registrado un juego con {} cifras".format(nombre, cifras))
                print("Digite un diferente numero de cifras!")
                break
        f.close()
        return no_juega
