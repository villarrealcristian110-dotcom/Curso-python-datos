print("Hola mundo")

producto = "ornitorrinco y transmilenio"
print(producto[0])
print(producto[1])
print(producto[2])
print(producto[3])
print(producto[4])
print(producto[5])
print(producto[6])
print(producto[7])
print(producto[8])
print(producto[9])

print(f"el producto es: {producto}")

print(producto[-3])
longitud = len(producto)
print("la longitud de la cadena de texto es", longitud)

#mayusculas y minusculas
print(producto.upper())#mayuscula
print(producto.lower())#mayuscula

#capitalizar - poner la primera letra en mayuscula
print(producto.capitalize())

print(producto.replace("y", "+"))#REEMPLAZAR ALGO POR OTRA COSA

print(producto.strip())#Eliminar espacios al inicio y al final del texto

nombre = "    CRISTIAN CAMILO VILLARREAL GIL       "
print(f"El nombre del cliente es: {nombre.strip().title()}")#Limpieza de datos

nombres = [
    "MARIA GOMEZ",
    "juan  perez",
    "ANA LOPEZ"
]
variable_uno = nombres[0]
print(f"la consulta del primer nombre es: ",variable_uno)
print(f"la limpieza del segundo nombre es: {nombres[1].strip()}")

### LISTAS
lista = ["monitor", "teclado", "mouse"]
print(lista)

lista.append("impresora") #AÑADIR ELEMENTOS EN LA LISTA
print(lista)

lista.insert(1, "disco duro")#AÑADIR ELEMENTOS EN UNA POSICION ESPECIFICA
print(lista)

lista.remove("teclado")#ELIMINAR ELEMENTOS ESPECIFICOS
print(lista)

del lista[2]#ELIMINAR ELEMENTOS DE UNA POSICION ESPECIFICA
print(lista)

lista.sort()#ORDENR POR ORDEN ALFABETICO
print(lista)

lista.append("teclado")
lista.append("Mouse")

lista.sort(reverse=True)#ORDENAR EN ORDEN ALFABETICO DE FORMA DESCDENTE
print(lista)

### UNIR LISTAS

lista2 = ["teclado inalambrico","mouse inalambrico", "pendrive"]
lista3 = lista + lista2
print(lista3)

#CONVERTIR UNA CADENA DE TEXTO EN UNA LISTA
cadena = "monitor , teclado, mouse, pendrive"
lista4 = cadena.split(",")
print(lista4)

print(len(lista4))#contar la cantidad de elementos de una lista

#crear una lista
#consultar un elementos
#modificar un elemento
#agregar un elemento
#eliminar un elemento

dias_ventas = ["lunes", "martes", "Miercoles", "Jueves", "Viernes"]
unidades_ventas = [200, 300, 250, 150, 300]
print("el dia ", dias_ventas[1], "se vendieron ", str(unidades_ventas[1]), " unidades")
dias_ventas[4] = "Sabado"#Remplazar
dias_ventas.append("Domingo")#Agregar
dias_ventas.remove("lunes")
print(dias_ventas)


