def main():
    telefono=input("inntroduce tu numero de telefono con prefijo y extension: ")

    if len(telefono)!=16:
        print("error al introducir número, debe tener prefijo y extensión")

    else:
        print("el número de telefono sin prefijo ni extensión es: {} ".format(telefono[4:13]))
if __name__=="main":
    main()