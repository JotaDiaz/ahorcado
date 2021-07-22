from random import *
from os import system, times
import time
def cleanScreen(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def data():
    palabras = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.upper()
            line = line.rstrip()
            palabras.append(line)
        return palabras

   
    
def run():
    palabra_azar = choice(data())

    nombre = input("¿Cual es tu nombre? ")
    nombre = nombre.upper()
    reglas = f"""
        
        BIENVENIDO AL AHORCADO {nombre}!
        
    Las reglas son simples, tenes que adivir la palabra letra por letra
    si tenes un error perdes 1 vida
    Tenes 5 vidas
    """
    print(reglas)
    time.sleep(1)
    start = int(input("Presiona 1 cuando estes listo:" ))
    if start != 1:
        print("Lo siento el juego no puede comenzar si no presionar la opcion correcta")
    else:
        print("COMIENZA EL JUEGO!!")
    aciertos = []
    errores = []
    vidas = 5
    print("_" * len(palabra_azar))
   
    while True:
        letra_a_letra = input("PRUEBA UNA LETRA: ")
    
        if len(letra_a_letra) != 1 or letra_a_letra.isnumeric():
            print("solo puedes ingresar LETRAS, de una en una.")
        elif letra_a_letra.lower() in aciertos:
                print("ya habia ingresado a esa letra intenta con otra")
        if letra_a_letra in palabra_azar:
            


        
        









if __name__ == '__main__':
    run()