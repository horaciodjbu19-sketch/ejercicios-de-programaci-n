# Ejercicio 2. Cálculo del tiempo de estancia


print("=== TIEMPO DE ESTANCIA ===")
print("Hora de entrada")
hora_entrada = int(input("  Hora (0-23): "))
min_entrada = int(input("  Minutos (0-59): "))

print("Hora de salida")
hora_salida = int(input("  Hora (0-23): "))
min_salida = int(input("  Minutos (0-59): "))


total_entrada = hora_entrada * 60 + min_entrada
total_salida = hora_salida * 60 + min_salida


if total_salida < total_entrada:
    total_salida = total_salida + 24 * 60

minutos_estancia = total_salida - total_entrada
horas_estancia = minutos_estancia / 60


print(f"Tiempo transcurrido: {minutos_estancia // 60} h {minutos_estancia % 60} min")
print(f"Tiempo en horas: {horas_estancia:.2f} horas")
