# Ejercicio 5. Descuentos para clientes frecuentes



print("=== DESCUENTO PARA CLIENTES FRECUENTES ===")
visitas = int(input("Número de visitas del cliente en el mes: "))
importe = float(input("Importe de la estancia: $"))

if visitas > 10:
    descuento = importe * 0.10
    print("Cliente frecuente: se aplica 10% de descuento.")
else:
    descuento = 0
    print("Cliente regular: tarifa normal.")

total = importe - descuento


print(f"Importe de la estancia: ${importe:.2f}")
print(f"Descuento:              ${descuento:.2f}")
print(f"Total a pagar:          ${total:.2f}")
