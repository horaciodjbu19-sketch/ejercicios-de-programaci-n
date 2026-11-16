# Ejercicio 3 . Cobro por tiempo de permanencia


TARIFA_HORA = 15

print("=== COBRO POR PERMANENCIA ===")
horas = float(input("Tiempo de permanencia en horas (puede tener decimales): "))


horas_cobradas = int(horas)
if horas > horas_cobradas:
    horas_cobradas = horas_cobradas + 1


if horas_cobradas == 0:
    horas_cobradas = 1

importe = horas_cobradas * TARIFA_HORA


print(f"Horas a cobrar: {horas_cobradas}")
print(f"Tarifa por hora: ${TARIFA_HORA}")
print(f"Importe a pagar: ${importe}")
