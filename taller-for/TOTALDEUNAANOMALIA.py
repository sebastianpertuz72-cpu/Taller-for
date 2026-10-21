"""
Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.
Fórmula o relación: Nómina = sueldo1 + sueldo2 + ... + sueldon.

"""

cantidad_emp= int(input("cantidad de empleados"))

suma = 0.0

if  0 <= cantidad_emp <= 1000:
    for veces in range(1, cantidad_emp+1):
        print("Empleado #", veces)
        sueldo= float(input("Sueldo? "))
        suma = suma + sueldo #<- acumuladores 

else:
    print("no valido")
print("La nomina es:", suma)