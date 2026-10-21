"""
Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros.
Cada registro contiene identificador entero positivo único, minutos enteros no negativos,
segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la
velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En
empate de tiempo gana el primero recibido.
Fórmula o relación: Tiempo en segundos T = 60 × minutos + segundos + centésimas/100;
velocidad = 900/T. Menor T determina el ganador.
"""

n = int(input("Ingrese el número de ciclistas: "))
identificador = 0
ganador = 0
id_ganador = 0

if 1 <= n <= 20:
    for i in range(n):
        identificador = int(input("Ingrese el identificador del ciclista: "))
        minutos = int(input("Ingrese los minutos del tiempo: "))
        segundos = int(input("Ingrese los segundos del tiempo: "))
        centesimas = int(input("Ingrese las centésimas del tiempo: "))

        ts = 60 * minutos + segundos + centesimas / 100
        velocidad = 900 / ts

        print(identificador, ":", velocidad, " km/h")
        if velocidad > ganador:
            ganador = velocidad
            id_ganador = identificador