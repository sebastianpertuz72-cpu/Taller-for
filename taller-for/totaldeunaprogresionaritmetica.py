"""

Se conoce el primer término A, la diferencia D y la cantidad N de términos de una
progresión. A y D son enteros entre -100 y 100, y N está entre 0 y 1000. Determine la suma de
los N términos; si N es cero, el total es cero.

Fórmula o relación: t1 = A; tk+1 = tk + D; S = t1 + t2 + ... + tn.

"""

A = int(input("Ingrese el termino A"))
B = int(input("Ingrese la diferencia D"))
X = int(input("Ingrese la cantidad N"))

if -100 < A < 100 and -100 < B < 100 and 0 <= X < 1000:
    t = A
    suma = 0
    for k in range(X):
        suma = suma + t
        t = t + B

    print(suma)
else:
    print("Valores inválidos")