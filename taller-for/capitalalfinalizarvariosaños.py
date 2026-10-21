"""
Una inversión ficticia inicia con capital C no negativo y mantiene una tasa anual
porcentual I con 0 < I < 100. Se recibe también un entero M entre 0 y 50.
El interés de cada año

es el saldo al comienzo de ese año multiplicado por I y dividido entre 100; se suma al saldo al
final del año.
 Determine el saldo después de M años;
con M = 0 conserva el capital inicial.
Fórmula o relación: Saldo nuevo = saldo anterior × (1 + I/100).

"""

C = int(input("Ingrese su capital no negativo"))
I = int(input("La tasa anual porcentual"))
M = int(input("Ingrese la cantidad de años"))


saldo = C

if M == 0:
    print("su capital es:", C)
elif C >= 0 and 0 < I < 100 and 0 <= M <= 50:
    for K in range(M):
        saldo=saldo * (1 + I/100)

    print("SALDO:", saldo)
    