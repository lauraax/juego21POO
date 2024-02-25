from juego21 import *

print("***Bienvenido a el juego de 21***")

juego= Juego()
juego.iniciar_juego()
juego.mostrar_juego_jugador()
juego.mostrar_juego_casa(False) 


while juego.jugador.dar_valor() <= 21:
    pedir = str(input("¿Desea agregar otra carta?: (1 para SI / 2 para NO ) \n"))
    if pedir == '1':
          juego.jugador.agregar_carta(juego.mazo.dar_carta())
          juego.mostrar_juego_jugador()
    else:
         break
    
if juego.jugador.dar_valor() > 21: 
      print("\n Tu juego superó los 21 puntos, perdiste \U0001F61E")
else: 
      
      while juego.casa.dar_valor() < 17:
            juego.casa.agregar_carta(juego.mazo.dar_carta())

      juego.mostrar_juego_jugador()
      juego.mostrar_juego_casa(True)

      valor_mano_jugador = juego.jugador.dar_valor()
      valor_mano_casa = juego.casa.dar_valor()
 
      if valor_mano_jugador > valor_mano_casa or valor_mano_casa > 21:
        print("\n FELICIDADES, LE GANASTE A LA BANCA", "\nValor de tu mano: ", valor_mano_jugador, "\nValor mano Casa: ", valor_mano_casa)
      elif valor_mano_jugador < valor_mano_casa:
        print("\n Tu mano es inferior a la de la casa, perdiste", "\U0001F61E", "\nValor de tu mano: ",valor_mano_jugador, "\nValor mano Casa: ", valor_mano_casa)
      else:
        print("\n EMPATE, gana la Casa","\nValor de tu mano: ",valor_mano_jugador,"\nValor mano Casa: ", valor_mano_casa)
