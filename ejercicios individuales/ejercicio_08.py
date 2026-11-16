# Ejercicio 8 . Corte de caja


print("=== ATENCIÓN DE VEHÍCULOS ===")

total_vehiculos = 0
motocicletas = 0
automoviles = 0
camionetas = 0
camiones = 0
total_recaudado = 0

continuar = "s"
while continuar == "s":
    
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

    
    total_vehiculos = total_vehiculos + 1
    total_recaudado = total_recaudado + importe
    if opcion == "1":
        motocicletas = motocicletas + 1
    elif opcion == "2":
        automoviles = automoviles + 1
    elif opcion == "3":
        camionetas = camionetas + 1
    else:
        camiones = camiones + 1

    continuar = input("¿Desea registrar otro vehículo? (si/no): ").lower()


print("========== CORTE DE CAJA ==========")
print(f"Total de vehículos atendidos: {total_vehiculos}")
print(f"Motocicletas:                 {motocicletas}")
print(f"Automóviles:                  {automoviles}")
print(f"Camionetas:                   {camionetas}")
print(f"Camiones:                     {camiones}")
print(f"Importe total recaudado:      ${total_recaudado}")
print("===================================")
