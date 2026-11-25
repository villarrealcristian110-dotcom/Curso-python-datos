#SESION 6
#IF
cantidad_productos = 3
if cantidad_productos <= 3:
    print("Bajo Stock")

#IF/ELSE
total_compra = 150000
if total_compra >= 2100000:
    print("Descuento autorizado")
else:
    print("No aplica descuento")
#EDUCACION
#LA NOTA ES IGUAL O SUPERIOR A 3.0?
#TRUE: ALCANZA EL CRITERIO
#FALSE: REQUIERE ESFUERZO

nota_alcanzada = 3.5
if nota_alcanzada >= 3:
    print("Aprobaste el curso")
else:
    print("Esfuerzate mas")

#EJERCICIO
stock_inventario = 6
if stock_inventario == 0:
    print("Inventario agotado")
elif stock_inventario <=5:
    print("Inventario bajo")
else:
    print("Inventario disponible")

#EJERICIO 2

total_compra = 150000
cliente_frecuente = False

if total_compra >= 100000 and cliente_frecuente:
    print("Descuento autorizado")
else:
    print("No cumple las condiciones")

usuario = {"nombre": "Ana", "rol": "admin"}

if usuario["rol"] == "admin":
    print(f"{usuario['nombre']} tiene acceso total")
elif usuario["rol"] == "editor":
    print(f"{usuario['nombre']} puede editar")
else:
    print(f"{usuario['nombre']} solo puede leer")
