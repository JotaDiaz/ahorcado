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
    palabra_azar = list(choice(data()))
    

    nombre = input("¿Cual es tu nombre? ")
    nombre = nombre.upper()
    reglas = f"""
        
        BIENVENIDO AL AHORCADO {nombre}
        
    Las reglas son simples, tenes que adivinar la palabra letra por letra
    si tenes un error perdes 1 vida
    Tenes 10 vidas
    """
    print(reglas)
    
    start = input("Presiona enter cuando estes listo")
    if start == any: 
        pass
    else:
        print("COMIENZA EL JUEGO!!")
    letras_utilizadas = []
    vidas = 6
    
    progreso = []

    for i in range(len(palabra_azar)):
        progreso.append("_ ")
    while vidas > 0:
        print(''.join(progreso))
        print('Letras utlizadas:', letras_utilizadas)
        print("\n")
        letra_a_letra = input("PRUEBA UNA LETRA: ")
        letra_a_letra = letra_a_letra.lower()
        
        errores = True
        for i in range(len(palabra_azar)):
                if letra_a_letra == palabra_azar[i]:
                    progreso[i] = letra_a_letra
                    
        
            

        if len(letra_a_letra) != 1 or letra_a_letra.isnumeric():
            errores = False
            print("solo puedes ingresar LETRAS, de una en una.")

            
        if letra_a_letra.lower() in letras_utilizadas:
            errores = False
            print("ya habia ingresado a esa letra intenta con otra")
            
            
            
        else:
            letras_utilizadas.append(letra_a_letra)

        if letra_a_letra not in palabra_azar and errores == True:
            vidas = vidas -1
            print('ERROR!! VIDAS RESTANTES:', vidas)
        
        
           

        
        
        if palabra_azar == progreso:
            print('Felicidades, has ganado!!la palabra secreta era', ''.join(palabra_azar))
            break
        elif vidas == 0:
            print('Juego terminado te quedaste sin vidas!! la palabra secreta era', ''.join(palabra_azar))
            break


        

        
        

    

        

        

        

        

              
            
        
        



            

if __name__ == '__main__':
    run()