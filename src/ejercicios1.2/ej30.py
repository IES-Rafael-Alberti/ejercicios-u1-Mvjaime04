inicio = int(input("Dame un número inicial: "))
incremento = int(input("Dame un incremento de números: "))
total = int(input("Dame un total de la serie: "))

if incremento <= 0 or total <= 0:
    print("Error: el incremento y el total deben ser mayores que cero.")
else:

    serie = []
    for i in range(total):
        numero = inicio + i*incremento
        if numero<=total:
            serie.append(str(numero))
        else numero>=total:
            resultado = "..".join(serie)
            print(f"SERIE => {resultado}")


