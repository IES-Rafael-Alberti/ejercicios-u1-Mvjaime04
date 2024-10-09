def main():
    fecha=int(input("Escribe tu fecha de nacimiento(dd/mm/aaaa): "))
    partes=fecha.split("/")

    if len(partes) !=3:
        print("formato incorrecto.usa el formato dd/mm/aaaa")
        
    dia=partes[0].zfill(2)
    mes= partes[1].zfill(2)
    año= partes[2]

    if len(año)!=4:
        print("formato incorrecto.usa el formato dd/mm/aaaa")

    print("naciste el dia {} del mes {} del año {}".format(dia,mes,año))

if __name__=="__main__":
    main()