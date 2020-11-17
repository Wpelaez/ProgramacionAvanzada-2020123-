from numero import Numero
from juego import Juego
from archivo import Archivo


numero_objeto = Numero()
Jugador = Juego()
archivo_objeto = Archivo()

verificar_nombre = True
while (verificar_nombre):
    Jugador.asignar_numeroAzar(numero_objeto.generar_lista_azar())
    verificar_nombre = archivo_objeto.verificar_usuario_cifras(Jugador.nombre, len(Jugador.numero_azar))

intentos = Jugador.numeroIntentos()

for intentos_ciclo in range(intentos):
    if(Jugador.gano!=True):
        print("Intento Numero {}".format(intentos_ciclo+1))
        Jugador.asignar_numeroJugador(numero_objeto.generar_lista_usuario(len(Jugador.numero_azar)))
        Jugador.jugar(intentos_ciclo)
        archivo_objeto.escribir(Jugador.nombre, len(Jugador.numero_azar),
                                intentos_ciclo + 1, Jugador.picas,
                                Jugador.fijas, Jugador.gano)
    else:
        break

if Jugador.gano:
    print("Victoria!")
else:
    print("No pudiste decifrar el numero!")

archivo_objeto.lider_cifras(len(Jugador.numero_azar))

