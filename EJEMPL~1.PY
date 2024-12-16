Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Clase base Personaje
... class Personaje:
...     def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
...         self.nombre = nombre
...         self.fuerza = fuerza
...         self.inteligencia = inteligencia
...         self.defensa = defensa
...         self.vida = vida
... 
...     def mostrar_atributos(self):
...         print(self.nombre, ":")
...         print("·Fuerza:", self.fuerza)
...         print("·Inteligencia:", self.inteligencia)
...         print("·Defensa:", self.defensa)
...         print("·Vida:", self.vida)
... 
...     def subir_nivel(self, fuerza, inteligencia, defensa):
...         self.fuerza += fuerza
...         self.inteligencia += inteligencia
...         self.defensa += defensa
... 
...     def esta_vivo(self):
...         return self.vida > 0
... 
...     def morir(self):
...         self.vida = 0
...         print(self.nombre, "ha muerto")
... 
...     def calcular_daño(self, enemigo):
...         return self.fuerza - enemigo.defensa
... 
...     def atacar(self, enemigo):
...         daño = self.calcular_daño(enemigo)
...         enemigo.vida -= daño
...         print(self.nombre, "ha infligido", daño, "puntos de daño a", enemigo.nombre)
...         if enemigo.esta_vivo():
...             print("Vida de", enemigo.nombre, "es", enemigo.vida)
...         else:
...             enemigo.morir()


# Clase Guerrero heredada de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma

    def cambiar_arma(self):
        print("Elige un arma: (1) Espada de Fuego, daño 12. (2) Hacha de Hierro, daño 8")
        opcion = int(input())
        if opcion == 1:
            self.arma = 12
        elif opcion == 2:
            self.arma = 8
        else:
            print("Opción incorrecta")

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print("·Arma:", self.arma)

    def calcular_daño(self, enemigo):
        return self.fuerza * self.arma - enemigo.defensa


# Clase Mago heredada de Personaje
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, hechizo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.hechizo = hechizo

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print("·Hechizo:", self.hechizo)

    def calcular_daño(self, enemigo):
        return self.inteligencia * self.hechizo - enemigo.defensa


# Función para simular el combate
def combate(jugador1, jugador2):
    turno = 0
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de", jugador1.nombre, ":")
        jugador1.atacar(jugador2)
        print(">>> Acción de", jugador2.nombre, ":")
        jugador2.atacar(jugador1)
        turno += 1

    if jugador1.esta_vivo():
        print("\nHa ganado", jugador1.nombre)
    elif jugador2.esta_vivo():
        print("\nHa ganado", jugador2.nombre)
    else:
        print("\nEmpate")


# Creación de personajes
personaje1 = Guerrero("Thor", 18, 8, 6, 100, 10)
personaje2 = Mago("Merlin", 6, 18, 4, 100, 3)

# Mostrar atributos de los personajes
personaje1.mostrar_atributos()
personaje2.mostrar_atributos()

# Iniciar el combate
combate(personaje1, personaje2)
[DEBUG ON]
[DEBUG OFF]
