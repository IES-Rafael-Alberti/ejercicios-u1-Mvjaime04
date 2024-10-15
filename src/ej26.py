def main():
    productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")


    lista_productos = [producto.strip() for producto in productos.split(",")]


    for producto in lista_productos:
        print(producto)

    if __name__=="__main__":
        main()