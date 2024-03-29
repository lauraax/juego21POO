from juego21poo import *

class Juego:
    def __init__(self):
        self.mazo = Mazo()
        self.casa = Mazo(True)
        self.jugador = Mazo(True)
    
    def iniciar_juego(self):
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
    
    def mostrar_juego_jugador(self):
        print("\n Tu mazo: ")
        self.jugador.mostrar_cartas(True) 
    
    def mostrar_juego_casa(self, mostrar = False):
        print("\n Mazo de la casa: ")
        if mostrar:
            self.casa.mostrar_cartas(True)
        else:
            self.casa.mostrar_cartas()
         
        
    


    
    