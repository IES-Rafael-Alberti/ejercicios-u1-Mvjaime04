interes = 0.04


capital = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))


ahorros_año_1 = capital * (1 + interes)
ahorros_año_2 = ahorros_año_1 * (1 + interes)
ahorros_año_3 = ahorros_año_2 * (1 + interes)

print("los ahorros a lo largo de 3 años seran de: ")
print(f"Ahorros al final del primer año: {ahorros_año_1:.2f}")
print(f"Ahorros al final del segundo año: {ahorros_año_2:.2f}")
print(f"Ahorros al final del tercer año: {ahorros_año_3:.2f}")

