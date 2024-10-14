def main():
    inicio = int(input("Introduce un número: "))
    incremento = int(input("Introduce el incremento: "))
    total = int(input("Introduce el número final de la serie: "))

    while incremento <= 0:
        print("Incremento no puede ser 0 o menor a cero")
        incremento = int(input("Introduce el incremento: "))

    while total <= 0:
        print("El segundo numero no puede ser 0 o menor a cero")
        total = int(input("Introduce el segundo número: "))

    serie = ""

    for i in range(total):
        cont = inicio + (i * incremento)  
        if i == 0:
            serie += str(cont) + '-'
        elif i == total - 1:
            serie += '-' + str(cont)
        elif i == 1:
            serie += str(cont)
        else:
            serie += '..' + str(cont)
    print(f"SERIE => {serie}")
if __name__=="__main__":
    main()