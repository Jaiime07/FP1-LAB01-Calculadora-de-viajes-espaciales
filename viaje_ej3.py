edad = int(input("tu edad es:"))
estado_fisico = int(input("Tu estado físico es:"))
if estado_fisico < 0 or estado_fisico > 10:
    print("Por favor, introduzca un valor válido")
    
elif edad >= 18 and estado_fisico >= 5:
    print("¡Listo para despegar!")
elif edad < 18:
    print("Debes ser mayor de edad!")
elif estado_fisico < 5:
    print("Debes mejorar tu estado físico!")