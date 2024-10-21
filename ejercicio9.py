"""
Programa que calcula cuanto deberá pagar un cliente en una tienda que ofrece un descuento del 15% sobre el total de la compra.
	Entrada: 	
		Total de la compra: int
	Salida:
		Total a pagar
"""
T_compra = int(input("Ingresa el total de la compra: "))
descuento = (T_compra * 15)/ 100
total = T_compra - descuento
print ("El total a pagar con descuento es: ", total)