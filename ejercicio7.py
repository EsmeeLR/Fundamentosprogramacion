"""
Programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde
"""
print ("Convierte una cantidad de minutos a horas")

minutos = int(input("Ingrese la cantidad en  minutos: "))
horas = minutos // 60
minres = minutos % 60
print ("Los minutos equivalen a:", horas,"horas y", minres, "minutos. .")


