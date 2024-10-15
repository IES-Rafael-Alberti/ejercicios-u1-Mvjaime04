def main():
    nombre=input("Dime tu nombre: ")
    edad=int(input("Dime tu edad: "))

    if nombre.strip()=="":
        nombre= "desconocido"

    if edad<0 or edad>125:
         print("error vuelva a introducir edad")
    else:
        cont=125-edad
        print(f"Te llamas {nombre} y tienes {edad} años, te quedan {cont} años por cumplir.")
if __name__=="__main__":
    main()