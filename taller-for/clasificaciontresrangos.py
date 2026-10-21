"""
Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada
una.
Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo.


Fórmula o relación: Grupo 1: v ≤ 200; grupo 2: 200 < v < 400; grupo 3: v ≥ 400.

"""
n = int(input("Ingrese la cantidad de ventas")) 

g1 = 0
g2 = 0
g3 = 0

if 0 <= n <= 1000:
    for i in range(n):
        importe = int(input("Ingrese el importe de venta", ))

        if importe <= 200:
            g1 += 1

        elif 200 < importe < 400:
            g2 += 1

        elif importe >= 400:
            g3 += 1
        
    print("grupo 1", g1)
    print("grupo 2", g2)
    print("grupo 3", g3)
