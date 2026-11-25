#sesion 7
#ciclo for
guias = ["G001", "G002", "G003", "G004", "G005"]

for memorias in guias:
    print("Revisando envío:", memorias)

#for + range

for consecutivo in range(2):
    print("revisando envío:", guias[consecutivo])

for consecutivo in range(3,4):
    print("Revisando envío:", guias[consecutivo])

#CONTADORES
contador = 0
for guia in guias:
    contador += 1
    print("Revisando", guia)



print("Total", contador)

# ACUMULADORES - CONTAR ENTEROS
# EJEMPLO: acumulador de kilometros
distancias = [15, 22, 10, 18]
distancia_total = 0
for suma_distancia in distancias:
    distancia_total += suma_distancia

print("Distancia Total: ", distancia_total)



envios = [
    {"estado": "entregado"},
    {"estado": "en ruta"},
    {"estado": "devuelto"},
    {"estado": "entregado"},
    {"estado": "devuelto"},
    {"estado": "entregado"},
]

entregados = 0
en_ruta = 0
devueltos = 0

for envio in envios:
    if envio["estado"] == "entregado":
        entregados += 1

    elif envio["estado"] == "en ruta":
        en_ruta +=1

    else:
        devueltos +=1

#MOSTARR RESULTADOS
print("RESUMEN DE ENVIOS")
print("Entregados: ", entregados)
print("En ruta: ", en_ruta)
print("Devueltos: ", devueltos)

# SEGUNDO CICLO: WHILE - "Mientras sea verdadero"-el ciclo se rompe cuando haya algo falso
#Intentos de entrega

guia = "G001"

intentos = 0

while intentos <3 and entregados == False:
    intentos += 1

    print("guia, guia")
    print("intentos de entrega", intentos)

resultado =input("se entrego el paquete? (S/N):     ").lower()

if resultado == "s":
    entregado = True
else:
    entregado = False

if entregado:
    print("Envio entregado")
else:
    print("Envio devuelto ")


#FRECUENCIA DE ENTREGAS EN TIEMPO
tiempos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

grupo_1_3 = 0
grupo_4_6 = 0
grupo_7_9 = 0
grupo_10_12 = 0

for tiempo in tiempos:
    if 1 <= tiempo <=3:
        grupo_1_3 +=1
    elif 4 <= tiempo <=6:
        grupo_4_6 +=1
    elif 7 <=tiempo <=9:
        grupo_7_9 +=1
    elif 10 <= tiempo <=12:
        grupo_10_12 +=1

print("REPORTE DE TIEMPOS DE ENTREGA")
print("de 1 a 3 dias ", grupo_1_3, "entregas")
print("de 1 a 3 dias ", grupo_4_6, "entregas")
print("de 1 a 3 dias ", grupo_7_9, "entregas")
print("de 1 a 3 dias ", grupo_10_12, "entregas")

persona = {"nombre": "Ana", "edad": 30, "ciudad": "Bogotá"}
print(persona)
usuario = {"nombre": "Sofía", "edad": 28, "ciudad": "Bogotá"}
print(usuario["nombre"])  # Salida: Sofía
