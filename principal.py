from juego21 import *

print("***Bienvenido a el juego de 21***")

juego= Juego()
juego.iniciar_juego()
juego.mostrar_juego() 


while juego.jugador.dar_valor()<=21:
    pedir = str(input("¿Desea agregar otra carta?: (1 para SI / 2 para NO ) \n"))
    if pedir == '1':
          juego.jugador.agregar_carta(juego.mazo.dar_carta())
    else:
         break
   

    
print (juego.jugador.dar_valor())
juego.mostrar_juego()
