# Solicitar al usuario que introduzca dos números enteros
n = int(input("Introduce el primer número entero (n): "))
m = int(input("Introduce el segundo número entero (m): "))

# Verificar que m no sea cero para evitar división por cero
if m == 0:
    print("Error: No se puede dividir por cero.")
else:
    # Calcular el cociente y el resto
    c = n // m  # Cociente
    r = n % m   # Resto

    # Mostrar el resultado
    print(f"La división de {n} entre {m} da un cociente {c} y un resto {r}.")