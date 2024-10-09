def main():   
    nombre_producto = input("Introduce el nombre del producto: ")
    precio_unitario = float(input("Introduce el precio del producto: "))
    numero_unidades = int(input("Introduce el número de unidades: "))

    coste_total = precio_unitario * numero_unidades

    print(f"{nombre_producto}: Precio unitario: {precio_unitario:06.2f}, "
        f"Número de unidades: {numero_unidades:03}, "
        f"Coste total: {coste_total:08.2f}")

if __name__== "__main__":
   main()