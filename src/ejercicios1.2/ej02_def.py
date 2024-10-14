def genera_importe(importe):
    return("importe total: " + str(importe))

def main():

    Horas= int(input("horas de trabajo: "))
    Coste = int (input("Coste por Hora: "))

    importe_total = Horas * Coste
    resultado=genera_importe(importe_total)
    print(resultado)
    
if __name__=="__main__":
    main()



