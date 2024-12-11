#Genera un número aleatorio entre 1 y 10 y solicita al usuario que adivine el número. Usa if para verificar si acertó o no.
#Ejemplo: Entrada: 5 → Salida: "¡Felicidades, acertaste!" o "Intenta de nuevo.".

import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
#Inicializar 3 vidas para el jugador
vidas = 3

while vidas > 0:
    
    # Solicitar al usuario que adivine el número
    print('Adivina el número (entre 1 y 10).')
    print('Puedes ingresar RESET para volver a empezar')
    adivinanza = (input("o QUIT para terminar la partida:"))

    #Si el jugador ingresó una cadena
    if adivinanza == 'RESET' and vidas > 0:
        numero_aleatorio = random.randint(1, 10)  # Generar un nuevo número aleatorio
        vidas = 3
        print('')
        print("¡El juego ha sido reiniciado! Se ha generado un nuevo número.")
        print('')
    elif adivinanza == 'QUIT' and vidas > 0:
        print('')
        print(f'Te has rendido. El número era {numero_aleatorio}.')
        break
    
    # Verificar si el usuario ingresó un número
    if adivinanza.isnumeric() and vidas > 0:
        #Verificar que el jugador haya adivinado correctamente
        if int(adivinanza) == numero_aleatorio:
            print('')
            print("¡Felicidades, acertaste!")
            break 
        
        #Si el jugador se equivocó, decirle si debe adivinar un número mayor o menor
        #y quitarle una vida
        elif int(adivinanza) != numero_aleatorio:
            vidas = vidas-1
            if int(adivinanza) < numero_aleatorio:
                print('')
                print(" El número que buscas es mayor. Intenta de nuevo.")
                print(f'Te quedan {vidas} intento/s')
                print('')
            elif int(adivinanza) > numero_aleatorio:
                print('')
                print(" El número que buscas es menor. Intenta de nuevo.")
                print(f'Te quedan {vidas} intento/s')
                print('')
    
    else :
        print('')
        print("Comando no admitido.")
        print('')

#Mensaje de fin del juego si se acaban las vidas
if vidas == 0:
        print('')
        print('Te has quedado sin intentos.')
        print(f'El número era {numero_aleatorio}')