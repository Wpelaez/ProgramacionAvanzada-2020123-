class Persona:
    def __init__(self):
        self.nombre = ""

    def setNombre(self, nombre):
        self.nombre = nombre

    def presentar(self):
        print("Hola mi nombre es: {}".format(self.nombre))

    """"
    def getNombre(self):
        return self.nombre
    """
