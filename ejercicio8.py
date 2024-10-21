"""
Programa que calcula cuanto dinero obtendrá por concepto de comisiones por las tres
ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y 
comisiones un vendedor que recibe un sueldo base más un 10% extra por comisión de sus ventas.
"""
Sbase=float(input("Ingrese el sueldo base: "))
ven1=float(input("Ingrese el valor de la primera venta: "))
ven2=float(input("Ingrese de la segunda venta: "))
ven3=float(input("Ingrese el valor de la tercera venta: "))
tventas=ven1 + ven2 +ven3
com= tventas * 0.10
Stota= Sbase + com
print("El total que recibira el vendedor con la comision de las tres vevntas es:" , Stota)
