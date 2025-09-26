
distancia_km = int(input("¿Cuál será la distancia recorrida durante el viaje?"))
paradas = 0
for i in range(0, distancia_km, 150000):
    if i % 150000 == 0 and i > 0:
        print(f"Parada en {i}")
        paradas += 1
print(f"Número de paradas: {paradas} ")