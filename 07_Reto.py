#PROGRAMA CONTROL MANTENIMIENTO PREVENTIVO DE UNA FLOTA
#crear diccionario llamado flota
flota = {
    "v-101": 320,
    "v-102": 780,
    "v-103": 1250,
    "v-104": 1680,
    "v-105": 450,
    "v-106": 920,
    "v-107": 1420,
    "v-108": 1850,
    "v-109": 610,
    "v-110": 1100,
    "v-111": 250,
    "v-112": 1550,
}
#PUNTO- 2 -Recorrer los registros
for recorrer in flota:
    print("El vehiculo", recorrer)



#PUNTO 3 - Clasificar los vehiculos
de_0_a_499km = "uso reciente"
de_500_a_999km = "Seguimiento"
de_1000_a_1499km = "Programar revision"
de_1500_a_1999km = "prioridad alta"

for clasificacion in flota:
    if clasificacion < 500:
        de_0_a_499km +=1
    elif 4 <= tiempo <=6:
        de_500_a_999km +=1
    elif 7 <=tiempo <=9:
        de_1000_a_1499km +=1
    elif 10 <= tiempo <=12:
        de_1500_a_1999km +=1

print("REPORTE DE TIEMPOS DE ENTREGA")
print("de 0 a 499 KM hay", de_0_a_499km, "vehiculos")
print("de 500 a 999 KM hay", de_500_a_999km, "vehiculos")
print("de 1000 a 1499 KM hay ", de_1000_a_1499km, "vehiculos")
print("de 1500 a 1999 KM hay ", de_1500_a_1999km, "vehiculos")