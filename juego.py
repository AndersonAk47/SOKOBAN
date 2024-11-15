import fichas
import mov
import os

def imprimir_tablero(tablero):
   
   # limpiar_pantalla()

    print('    ', end='')
    for i in range(len(tablero[0])):
        print(f'{i + 1} ', end='')
    print()

    for i, fila in enumerate(tablero):

        print(f'{i + 1}  | ', end='')

        for columna in fila:
            print(columna, end=' ')

        print(f'| {i + 1}')

    print('    ', end='')
    for i in range(len(tablero[0])):
        print(f'{i + 1} ', end='')
    print()





def buscar_player(tablero):
    for i, fila in enumerate(tablero):
        for j, columna in enumerate(fila):
            if columna == fichas.PLAYER:
                return i, j
    return -1, -1


def mover_player(tablero, direccion):
    fila, columna = buscar_player(tablero)
    fila_obj, columna_obj = fila, columna

    if direccion == mov.ARRIBA:
        fila_obj -= 1 # fila = fila - 1
    elif direccion == mov.ABAJO:
        fila_obj += 1
    elif direccion == mov.IZQUIERDA:
        columna_obj -= 1
    elif direccion == mov.DERECHA:
        columna_obj += 1
    else:
        print('No se reconoce la direccion')

    if fila_obj < 0 or columna_obj < 0 or \
        fila_obj >= len(tablero) or columna_obj >= len(tablero[0]):
        print('Movimiento no valido')
        return
    

    if  tablero[fila_obj][columna_obj] == fichas.SPACE :
        tablero[fila][columna] = fichas.SPACE
        tablero[fila_obj][columna_obj] = fichas.PLAYER

    elif  tablero[fila_obj][columna_obj] == fichas.GOALS :
        tablero[fila][columna] = fichas.PLAYER
        tablero[fila_obj][columna_obj] = fichas.SPACE
 

    else:
        print('Movimiento no valido')


def win(tablero):
    victoria = True

    for fila in tablero:
        for columna in fila:
            if columna == fichas.CAJ or columna ==  fichas.GANADOR :
                victoria = False

    return victoria

def leer_direccion():
    """
    Lee la direcciÃ³n del usuario Numpy

    Retorno
    -------
        str: direcciÃ³n en la que va a mover el robot
    """
    direccion = input('Ingrese el movimiento (W/A/S/D) o X para salir: ')
    direccion = direccion.upper()

    if direccion == 'W':
        return mov.ARRIBA
    elif direccion == 'A':
        return mov.IZQUIERDA
    elif direccion == 'S':
        return mov.ABAJO
    elif direccion == 'D':
        return mov.DERECHA
    elif direccion == 'X':
        return mov.EXIT
    else:
        return leer_direccion()


def juego():
    tab = fichas.tablero
    imprimir_tablero(tab)
    direccion = leer_direccion()

    while direccion != mov.EXIT and not win(tab):
        mover_player(tab, direccion)
        imprimir_tablero(tab)
        direccion = leer_direccion()

    print('Chao')

juego()