def generar_cadena(nombre):
    return(f"hola {nombre}")

def main():
    nombre=input("dime tu nombre: ")
    resultado= generar_cadena(nombre)
    print(resultado)

if __name__=="__main__":
    main()