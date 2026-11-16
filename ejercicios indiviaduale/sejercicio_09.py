# Ejercicio 9 . Control de capacidad


CAPACIDAD = 30

print("=== CONTROL DE CAPACIDAD ===")

vehiculos_dentro = 0
continuar = "s"

while continuar == "s" and vehiculos_dentro < CAPACIDAD:
    print()
    print(f"Espacios disponibles: {CAPACIDAD - vehiculos_dentro}")
    placa = input("Placa: ")

    tarifa = 0
    while tarifa == 0:
        print("1. Motocicleta  2. Automóvil  3. Camioneta  4. Camión")
        opcion = input("Tipo de vehículo (1-4): ")
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
            print("Opción no válida, intente de nuevo.")

    horas = float(input("Horas de estancia: "))
    horas_cobradas = int(horas)
    if horas > horas_cobradas:
        horas_cobradas = horas_cobradas + 1
    if horas_cobradas == 0:
        horas_cobradas = 1

    importe = horas_cobradas * tarifa
    print(f"-> Placa {placa} ({tipo}): {horas_cobradas} h x ${tarifa} = ${importe} a pagar")

    vehiculos_dentro = vehiculos_dentro + 1

    if vehiculos_dentro < CAPACIDAD:
        continuar = input("¿Desea registrar otro vehículo? (si/no): ").lower()


if vehiculos_dentro >= CAPACIDAD:
    print("ESTACIONAMIENTO LLENO: no es posible recibir más vehículos.")
print(f"Vehículos registrados: {vehiculos_dentro}")
print(f"Espacios disponibles:  {CAPACIDAD - vehiculos_dentro}")
