
while True:
    distancia_km = int(input("Distancia:"))  # distancia Tierra - Luna
    velocidad_kmh = int(input("Velocidad:"))
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    pregunta = input("¿Quieres hacer otra simulación? (s/n)")
    if pregunta == "n":
       break
print("Buen viaje!")