solicitud = {"codigo": "ADM-004",
              "tipo": "actualizacion de datos",
              "area_solicitante":"talento humano",
              "dias pendiente":3,
              "afecta_operacion":True,
              "estado":"pendiente"}
if solicitud["estado"] == "pendiente":
    print("No requiere nueva gestion")
elif solicitud["afecta_operacion"] == True:
    print("Seguimos") 
else:
    print("finaliza el programa")


