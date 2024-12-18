"""
Primera Actividad Módulo 3: Proyecto - Piedra-Papel-Tijeras

Versión: 0.2.0
-------------------------------------

REGLAS:

Las reglas son sencillas: Los jugadores eligen simultáneamente uno de los tres signos: piedra, papel o tijera. El ganador se determina según las siguientes reglas: 

1.    El papel le gana a la piedra (“El papel envuelve a la piedra”).

2.    La piedra le gana a la tijera (“La piedra destruye a la tijera”).

3.    La tijera le gana al papel (“La tijera corta el papel)


Paso Nº 1: Creamos variables: 
    > contadoras: ronda_actual; puntaje_jugador, puntaje_compu y empates;

Paso Nº 2: Creamos el bucle principal:
    > agregamos una nueva variable de control, de tipo bool (verdadero o falso) llamada seguir_jugando
    > agregamos un bucle while(seguir_jugando)
      y dentro de éste un check para validar si el usuario desea continuar o no
"""

import time
import random

""" ··· [ Variables ] ··· """
puntaje_jugador = 0
puntaje_compu = 0
empates = 0

ronda_actual = 0
seguir_jugando = True
""" ····················· """

"""   ###################
     # BUCLE PRINCIPAL #
    ###################    """

while (seguir_jugando):

    # Paso Final: PREGUNTAMOS SI QUIERE SEGUIR JUGANDO
    
    seguir_jugando = input("\n ¿Desea seguir jugando? (S/N): ")
    
    if ('S' in seguir_jugando) or ('s' in seguir_jugando) or (seguir_jugando == ""):
        seguir_jugando = True
    
    else:
        seguir_jugando = False
        print("JUEGO FINALIZADO")