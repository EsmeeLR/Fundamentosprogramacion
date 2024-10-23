"""
Programa que permita obtener el
número invertido de un numero dado.
"""

a = int(input("Ingrese un número de dos cifras: "))

cifra_unidades = a % 10
cifra_decenas = a // 10
N_inv = cifra_unidades * 10 + cifra_decenas

print("El número invertido es:", N_inv)