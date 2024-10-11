"""
    Programa 2:
    Crear un programa que calcule área y perímetro de un rectángulo
Entradas:
    base: integer
    altura: integer
Salidas:
    area: integer
    perimetro: integer
"""
base = input ("Ingresa la base: ")
base = int(base)
altura = input ("Ingresa la altura: ")
altura = int(altura)
area = base * altura
perimetro = (base + altura) * 2
print("El área del rectángulo es", area)
print("El perímetro del rectángulo es", perimetro)
