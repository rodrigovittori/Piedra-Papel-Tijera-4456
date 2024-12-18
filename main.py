"""
Primera Actividad Módulo 3: Proyecto - Piedra-Papel-Tijeras

Versión: 0.5.0
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

Paso Nº 3: Pedir al Jugador su elección (piedra, papel o tijera)
    > Creamos una nueva variable (dentro del bucle) -> opcion_jugador
    > Pedimos su valor con input() y lo convertimos a int()
        > 1) Piedra
        > 2) Tijeras
        > 3) Papel

    > Creamos un bucle para verificar que la opción ingresada sea válida (opcion_jugador >= 0) and (opcion_jugador <= 3)
        > Si el valor NO es válido, lo solicitamos nuevamente
        > En cambio, si es válido, convertimos ese valor a su equivalente en texto:
            > 1: "Piedra" / 2: "Tijeras" / 3: "Papel"

Paso Nº 4: Generamos con random.randint(1-3) la respuesta de la computadora y la almacenamos en una nueva variable
           llamada opcion_compu; luego, la reemplazamos por el texto equivalente

Paso Nº 5: Evaluamos el resultado de la ronda. La consigna indica que debemos seguir el órden:
            > empate -> victoria (jugador) -> else: derrota (jugador)
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

    """ > Paso Nº 1: Pedir al jugador su elección """
    opcion_jugador = 0
    while ((opcion_jugador <= 0) or (opcion_jugador > 3)):
        opcion_jugador = int(input("\n Que eliges? \n (1) Piedra (2) Tijeras (3) Papel \n >"))

    """ > Paso Nº 2: Calcular la elección de nuestro bot / IA """
    opcion_compu = random.randint(1, 3)
    ronda_actual += 1

    """ > Paso Nº 3: Configuramos el texto """
    
    if (opcion_jugador == 1):
        opcion_jugador = "Piedra"
            
    elif (opcion_jugador == 2):
        opcion_jugador = "Tijeras"
            
    elif (opcion_jugador == 3):
        opcion_jugador = "Papel"
        
    else:
        opcion_jugador = "VALOR NO VALIDO"

    # COMPU    
        
    if (opcion_compu == 1):
        opcion_compu = "Piedra"
            
    elif (opcion_compu == 2):
        opcion_compu = "Tijeras"
            
    elif (opcion_compu == 3):
        opcion_compu = "Papel"
        
    else:
        opcion_compu = "VALOR NO VALIDO"

    """ * Pausa para generar suspenso* """
    time.sleep(3)

    """ * Espacio para insertar texto * """
    
    """ Paso Nº 4: DETERMINAR RESULTADO DE RONDA: """

    ## CASO 1: EMPATE
    if (opcion_jugador == opcion_compu):
        print("Es un empate :/")
    
    ## CASO 2: VICTORIA!
    elif ( ((opcion_jugador == "Piedra")  and (opcion_compu == "Tijeras")) or
           ((opcion_jugador == "Papel")   and (opcion_compu == "Piedra"))  or
           ((opcion_jugador == "Tijeras") and (opcion_compu == "Papel")) ):
        print("¡HAS GANADO! :D")
    
    ## CASO 3: DERROTA :(

    else:
        print("Has sido derrotado :(")

    """ * Espacio para insertar texto * """

    
    # Paso Final: PREGUNTAMOS SI QUIERE SEGUIR JUGANDO
    
    seguir_jugando = input("\n ¿Desea seguir jugando? (S/N): ")
    
    if ('S' in seguir_jugando) or ('s' in seguir_jugando) or (seguir_jugando == ""):
        seguir_jugando = True
    
    else:
        seguir_jugando = False
        print("JUEGO FINALIZADO")