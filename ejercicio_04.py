# Ejercicio 4 . Tarifas diferenciadas



print("=== TARIFAS DIFERENCIADAS ===")
horas = float(input("Tiempo de permanencia en horas: "))


horas_cobradas = int(horas)
if horas > horas_cobradas:
    horas_cobradas = horas_cobradas + 1
if horas_cobradas == 0:
    horas_cobradas = 1


if horas <= 2:
    tarifa = 20
elif horas <= 5:
    tarifa = 18
else:
    tarifa = 15

importe = horas_cobradas * tarifa


print(f"Tarifa aplicada: ${tarifa} por hora")
print(f"Horas a cobrar: {horas_cobradas}")
print(f"Importe a pagar: ${importe}")
