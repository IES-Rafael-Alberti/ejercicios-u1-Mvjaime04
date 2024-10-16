def calcula_precio(iva: float, importe: float) -> str:
    return f"El importe del articulo con IVA={iva:.2f} es de {importe:.2f} ."

def calcula_importe(articulo: float, iva_impuesto: float) -> float:
    return articulo * iva_impuesto

def main():
    articulo = int(input("Dime cual es tu importe sin IVA: "))
    iva_impuesto = float(input("Dime cual es tu IVA a aplicar: "))
    if iva_impuesto < 0 or iva_impuesto > 100:
        iva_impuesto = 0.21

    importe = calcula_importe(articulo, iva_impuesto)

    resultado = calcula_precio(iva_impuesto, importe)

    print(resultado)

if __name__ == "__main__":
    main()