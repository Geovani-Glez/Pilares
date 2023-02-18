#Proyecto Final Escuela de Codigo
#Juego del "Ahorcado"
#Luis Geovani Gonzalez Morales
import random

escenario = \
    '''   
~~~~~~~~~|~
         0
        213
         4
        56    
~~~~~~~~~~~   
'''

simbolos = "O|//|//"


def bienvenida():
    print('*' * 75)
    print('* Bienvenido al juego del ahorcado *')
    print('*' * 75)


def inicializar_juego(diccionario):
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []


def mostrar_escenario(errores):
    escena = escenario
    for i in range(0, len(simbolos)):
        simbolo = simbolos[i] if i < errores else ' '
        escena = escena.replace(str(i), simbolo)
    print(escena)


def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letras_erroneas) > 0:
        print('\n Letras erróneas:', *letras_erroneas)
        print()


def pedir_letra(tablero, letras_erroneas):
    valida = False
    while not valida:
        letra = input('\n Introduce una letra (a-z): ').lower()
        valida = 'a' <= letra <= 'z' and len(letra) == 1 # es una letra
        if not valida:
            print('Error, la letra tiene que estar entre a y z.')
        else:
            valida = letra not in tablero + letras_erroneas
            if not valida:
                print('Letra repetida, prueba con otra.')

    return letra


def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('\n ¡Bien! Has acertado una letra.')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print('\n \n ¡Oh! Has fallado.')
        letras_erroneas.append(letra)


def actualizar_tablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra


def comprobar_palabra(tablero):
    return '_' not in tablero


def jugar_al_ahorcado(diccionario):

    tablero, palabra, letras_erroneas = inicializar_juego(diccionario)
    while len(letras_erroneas) < len(simbolos): 
        mostrar_escenario(len(letras_erroneas))  
        mostrar_tablero(tablero, letras_erroneas) 
        letra = pedir_letra(tablero, letras_erroneas) 
        procesar_letra(letra, palabra, tablero, letras_erroneas) 
        if comprobar_palabra(tablero):  
            print('\n ¡FELICIDADES, lo has logrado!')
            break
    else:
        print(f'\n ¡Lo siento! ¡Has perdido! La palabra a adivinar era --> {palabra} ".')
        mostrar_escenario(len(letras_erroneas)) 

    mostrar_tablero(tablero, letras_erroneas)


def jugar_otra_vez():
    return input('\n Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ')


def despedida():
    print('*' * 75)
    print('* ¡Hasta pronto! *')
    print('*' * 75)


if __name__ == '__main__':

    diccionario = ['escuela', 'codigo', 'pilares', 'alumnos', 'profesora', 'computacion', 'talleres', 'programacion', 'python']

    bienvenida()
    while True:
        jugar_al_ahorcado(diccionario)
        if jugar_otra_vez() != 's': break
    despedida()
