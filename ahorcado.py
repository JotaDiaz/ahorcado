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
            line = line.lower()
            palabras.append(line)
            
        return palabras

   
    
def run():
    palabra_azar = choice(data())
    print(palabra_azar)

    nombre = input("¿Cual es tu nombre? ")
    nombre = nombre.upper()
    reglas = f"""
        
        BIENVENIDO AL AHORCADO {nombre}!
        
    Las reglas son simples, tenes que adivir la palabra letra por letra
    si tenes un error perdes 1 vida
    Tenes 10 vidas
    """
    print(reglas)
    time.sleep(1)
    start = input("Presiona enter cuando estes listo")
    if start == any: #no se para que sirve any pero funciona xd
        pass
    else:
        print("COMIENZA EL JUEGO!!")
    aciertos = []
    errores = []
    vidas = 10
    guin_bajo = "_" * len(palabra_azar)
    print(guin_bajo)
   
    while True:
        letra_a_letra = input("PRUEBA UNA LETRA: ")
    
        if len(letra_a_letra) != 1 or letra_a_letra.isnumeric():
            print("solo puedes ingresar LETRAS, de una en una.")
        else:
            if letra_a_letra.lower() in aciertos:
                print("ya habia ingresado a esa letra intenta con otra")
            else:
                aciertos.append(letra_a_letra)

                if letra_a_letra.lower() in palabra_azar:

                    print("Has acertado una letra")
                    
                else: 
                    vidas = vidas -1
                    print("Has perdido una vida, vidas restantes: " + str(vidas))




            

if __name__ == '__main__':
    run()
            


        
        









if __name__ == '__main__':
    run()