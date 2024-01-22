

import random
import string

from palabras_ingles import palabras
from ahorcado_diagramas import vidas_diccionario_visual

# Funcion que selecciona una palabra valida para el juego


def obtener_palabra_valida(lista_palabras):
    # seleccionar una palabra al azar de la lista
    palabra = random.choice(lista_palabras)
    # Si la palabra contiene un guión o un espacio,
    # seguir seleccionando una palabra al azar.
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(lista_palabras)
    return palabra.upper()  # regresa la palabra en mayusculas


def ahorcado():

    print("****************************************")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("****************************************")

    palabra = obtener_palabra_valida(palabras)
    # conjunto de letras de la palabra que deben ser adivinadas.
    letras_por_adivinar = set(palabra)
    # conjunto de letras en el abecedario.
    abecedario = set(string.ascii_uppercase)
    # letras que el usuario ha ingresado durante el juego.
    letras_ingresadas = set()

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:

        # ' '.join(['A', 'B', 'C']) --> 'A B C'
        print(
            f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_ingresadas)}")

        # Estado actual de la palabra que el jugador debe adivinar (por ejemplo:  H - L A)
        palabra_lista = [
            letra if letra in letras_ingresadas else '-' for letra in palabra]
        # Se muestran las que ya se adivinaron y las que no, se muestran como un "-" al inicio solo se mostrara -----

        # mostrar estado del ahorcado.
        # clave Num de Vidas, valor de retorno la "imagen" del diccionario
        print(vidas_diccionario_visual[vidas])

        # mostrar las letras actuales
        print(f"Palabra: {' '.join(palabra_lista)}")

        # El usuario escoge una letra nueva y se convierte en mayuscula
        letra_usuario = input("Escoge una letra: ").upper()

        # si la letra esta en el abecedario y no se a ingresado anteriormente
        # esto es no existe en (letras_ingresada) entonces
        # agregala a letras ingresada, estas letras son las que el usuario
        # ingresa, sean correctas o no
        if letra_usuario in abecedario - letras_ingresadas:  # resta de conjuntos
            letras_ingresadas.add(letra_usuario)

            # Si la letra está en la palabra, aqui validamos si es correcta o no, si esta en las
            # letras que se deben adivinar se quita de esa lista
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            # Si la letra no está en la palabra,no esta en las letras por adivinar, quitar una vida.
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        # Si la letra ingresada ya se repitio
        elif letra_usuario in letras_ingresadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

    # el juego termina si las vidas se acaban o si a acertado todas las letras por adivinar
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(
            f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


if __name__ == '__main__':

    while True:
        ahorcado()
        print(" ")
        op = input("Deseas terminar el Juego: ?  S/N ")
        if op.upper() == "S":
            break
    print("Juego Terminado Gracias por Jugar :3")
