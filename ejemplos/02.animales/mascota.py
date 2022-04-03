class Mascota():
    #nombre = ""
    #edad = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        # Aquí pueden ir más cosas que se hacen en un constructor

    def saludar(self):
        print("¡Hola! Me llamo {} y mi edad es {}".format(
            self.nombre, self.edad))


mascota = Mascota("Pluto", 3)
mascota.saludar()
otra_mascota = Mascota("Snowball", 1)
otra_mascota.saludar()