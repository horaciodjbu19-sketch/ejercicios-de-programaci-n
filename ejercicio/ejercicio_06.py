# Ejercicio 6 . Clasificación del tipo de vehículo



print("=== TARIFA POR TIPO DE VEHÍCULO ===")
print("1. Motocicleta")
print("2. Automóvil")
print("3. Camioneta")
print("4. Camión")
opcion = input("Seleccione el tipo de vehículo (1-4): ")

if opcion == "1":
    tipo = "Motocicleta"
    tarifa = 10
elif opcion == "2":
    tipo = "Automóvil"
    tarifa = 15
elif opcion == "3":
    tipo = "Camioneta"
    tarifa = 20
elif opcion == "4":
    tipo = "Camión"
    tarifa = 30
else:
    tipo = ""
    tarifa = 0

if tarifa == 0:
    print("Opción no válida. No se puede calcular el importe.")
else:
    horas = float(input("Horas de estancia: "))

    
    horas_cobradas = int(horas)
    if horas > horas_cobradas:
        horas_cobradas = horas_cobradas + 1
    if horas_cobradas == 0:
        horas_cobradas = 1

    importe = horas_cobradas * tarifa

    
    print(f"Tipo de vehículo: {tipo}")
    print(f"Tarifa por hora: ${tarifa}")
    print(f"Horas a cobrar: {horas_cobradas}")
    print(f"Importe a pagar: ${importe}")
