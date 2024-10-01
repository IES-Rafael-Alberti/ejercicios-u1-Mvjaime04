n=int(input("introduce n( n debe ser un num entero positivo): "))

if n > 0:
    # Calcular la suma utilizando la fórmula
    suma = n * (n + 1) // 2
    
    # Mostrar el resultado
    print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")
else:
    print("Por favor, introduce un número entero positivo.")    