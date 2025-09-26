distancia_km = 225000000  # distancia Tierra - Marte
for i in range(10000, 50000, 10000):
    velocidad_kmh = range(10000, 50000, 10000)
    tiempo_horas = distancia_km / i
    tiempo_dias = tiempo_horas / 24
    print(f"Velocidad: {velocidad_kmh} ----> Tardarías {tiempo_dias} en llegar")