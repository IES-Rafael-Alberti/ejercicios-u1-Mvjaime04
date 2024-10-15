def sumar_enteros(entero):
    if entero > 0:
    
        suma = entero * (entero + 1) // 2
    
    
        return(f"La suma de los enteros desde 1 hasta {entero} es: {suma}")
    else:
        return("Por favor, introduce un número entero positivo.") 
    
def main():
    n=int(input("introduce n( n debe ser un num entero positivo): "))

    resultado=sumar_enteros(n)

    print(resultado)
    
if __name__=="__main__":
    main()
