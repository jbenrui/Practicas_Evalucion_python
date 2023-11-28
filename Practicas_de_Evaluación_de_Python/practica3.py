# Realiza, utilizando Python 3, el ejercicio 3 de la pagina 35 del libro "Introduccion a
# Python de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
# debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
# cabeceras:
# def estaEnRango(valor, minimo, maximo)
#   Devuelve True o False determinando que valor se encuentra entre el minimo y el
#   maximo.
# def estaEnLista(valor, lista)
#   Devuelve True o False determinando si el valor esta en la lista.

def estaEnRango(valor, minimo, maximo):
    return valor >= minimo & valor <= maximo 
def estaEnLista(valor, lista):
    return valor in lista 

lista_numeros = [6, 14, 11, 3, 2, 1, 15, 19]

while True:
    try:
        num = int(input("Introduce un número del 1 al 20: "))
        if  not estaEnRango(num,1,20):
            print("El número debe estar entre 1 y 20.")
            continue
            
        if estaEnLista(num, lista_numeros):
            print(f"El número {num} esta en la lista.")
        else:
            print(f"El número {num} no esta en la lista.")
            
        break
    except ValueError:
        print("Por favor, introduce un número valido.")