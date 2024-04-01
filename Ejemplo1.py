camisetas= { 1: ["polo", "blanca", 15],
            2: ["polo", "azul", 15],
            3: ["polo", "roja", 15],
            4: ["polo", "amarilla", 15],
            5: ["cuello redondo", "gris", 12],
            6: ["cuello redondo", "negro", 12],
            7: ["cuello redondo", "verde", 12]}

jeans = {1: ["Azul", 20],
         2: ["verde", 20],
         3: ["cafe", 20],
         4: ["negro", 20],
         5: ["gris", 20]}

zapatos = { 1: ["botas", "cafe", 25],
           2: ["tenis", "azul", 20],
           3: ["botas", "negro", 25],
           4: ["tenis", "blanco", 20]}

compras = []

def datos():
            while True:
                        nombre_apellido= input("Ingrese su nombre y apellido: ")
                        id= input("Ingrese su identificación (SOLO NÚMEROS): ")
                        tel= input("Ingrese su teléfono (SOLO NÚMEROS): ")
                        try:
                                    id=int(id)
                                    tel=int(tel)
                                    break
                        except ValueError: 
                                    print("Por favor, ingrese sólo números")
            direccion= input("Ingrese su dirección: ")
            return nombre_apellido, id, tel, direccion 
