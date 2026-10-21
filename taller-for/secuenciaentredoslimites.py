"""
Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.

"""

limiteA = int(input("Ingrese el limite A"))
limiteB = int(input("Ingrese el limite B"))

if limiteA < -100 and limiteB < 100 or limiteA > -100 and limiteB > 100:
    print("Numero no valido")
elif limiteA <= limiteB:
    print(list(range(limiteA, limiteB+1, 1))) 
elif limiteA > limiteB:
    print(list(range(limiteA, limiteB-1, -1))) 
