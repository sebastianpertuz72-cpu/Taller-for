"""
Se reciben N empleados, con 1 ≤ N ≤ 40. Cada registro contiene, en este orden,
identificador entero positivo único, edad entera no negativa en años y años enteros de
antigüedad entre 1 y 50. El sueldo ficticio es la suma de una base de 100 unidades monetarias,
el valor numérico de la edad y la suma de los enteros desde 1 hasta la antigüedad; toda esa
suma se divide entre los años de antigüedad. La edad y la suma de años se consideran aportes
numéricos en unidades monetarias dentro de este modelo ficticio. Informe el sueldo de cada empleado, el total de la nómina y los identificadores con mayor y menor sueldo. En empate
conserve el primero recibido.
Fórmula o relación: Sueldo = (100 + edad + (1 + 2 + ... + antigüedad))/antigüedad.
"""
n_empleados = int(input("Ingrese la cantidad de empleados: "))
suma_an = 0
sueldo = 0
mayor_sueldo = 0
menor_sueldo = 0
id_mayor_sueldo = 0
id_menor_sueldo = 0
total_nomina = 0

if 1 <= n_empleados <= 40:
    for i in range(n_empleados):
        identificador = int(input("Ingrese el identificador del empleado: "))
        edad = int(input("Ingrese la edad del empleado: "))
        antiguedad = int(input("Ingrese la antigüedad del empleado: "))

        if 1 <= antiguedad <= 50:
            for j in range(1, antiguedad + 1):
                print(j)
                suma_an += j

            sueldo = (100 + edad + suma_an)/antiguedad
            suma_an = 0
            if sueldo > mayor_sueldo:
                mayor_sueldo = sueldo
                id_mayor_sueldo = identificador
            else:
                menor_sueldo = sueldo
                id_menor_sueldo = identificador

            total_nomina += sueldo
            print(identificador, ": ", sueldo)

print("Nómina: ", total_nomina, " Mayor: ", id_mayor_sueldo, " Menor: ", id_menor_sueldo)