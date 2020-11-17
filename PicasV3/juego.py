class Juego():

    def __init__(self):
        self.nombre = input("Digite El nombre de jugador: ")
        self.numero_azar = []
        self.numero_usuario = []
        self.gano = False
        self.intentos = 0
        self.picas = 0
        self.fijas = 0

    def asignar_numeroAzar(self, numero_azar):
        self.numero_azar = numero_azar

    def asignar_numeroJugador(self, numero_usario):
        self.numero_usuario = numero_usario

    def numeroIntentos(self):
        cifras = len(self.numero_azar)
        if cifras == 3:
            intentos = 10
        elif cifras == 4:
            intentos = 15
        elif cifras == 5:
            intentos = 20
        else:
            intentos = 1
            print("ERROR")
        print("Tienes {} Intentos".format(intentos))
        return intentos

    def jugar(self, intento):
        self.intentos = intento
        self.fijas=0
        self.picas=0
        for i in range(len(self.numero_usuario)):
            if (self.numero_usuario[i] == self.numero_azar[i]):
                self.fijas+=1
            elif(self.numero_usuario[i] in self.numero_azar):
                self.picas+=1
        # print(self.numero_azar)
        print("Picas: {}".format(self.picas))
        print("Fijas: {}".format(self.fijas))
        if self.fijas == len(self.numero_azar):
            self.gano = True
        else:
            self.gano = False