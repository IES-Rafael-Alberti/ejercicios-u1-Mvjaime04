Importe_final= int(input("Dame el importe final de tu articulo: "))

IVA= Importe_final*10/100

print("El IVA que has pagado es de: "+ str(IVA)+ " y el importe sin IVA es de: "+ str(Importe_final/IVA))
