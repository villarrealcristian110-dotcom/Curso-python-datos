nombre = input("ingrese_su_nombre: ")
print(nombre)
mensaje = "Hola "+nombre + " Bienvenido al programa"
print(mensaje)

#Variables
edad = input("Por favor ingrese su edad: ")
print("su edad es : ",edad)

edad = int(edad)
edad = edad * 2
print("Su edad es: ", edad)

producto = "Audifonos"
print(producto)
Cantidad = input("Ingrese la cantidad que desea comprar: ")
print(Cantidad)
precio_unit = 20000
print(precio_unit)
mensajecompra = "los "+ producto + " tienen un valor de "+ str(precio_unit) + " Pesos Colombianos"
print(mensajecompra)
calcular_total = int(Cantidad) * precio_unit
print("el precio total de la compra es " + str(calcular_total))