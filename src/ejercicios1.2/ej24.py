def main():
    dinero=input("dime el precio del producto: ")
    separacion=dinero.split(".")
    euros= separacion[0]
    centimos= separacion[1]
    print("el precio de tu producto es de {} euros y {} centimos ".format(euros,centimos[0:2]))
if __name__=="__main__":
    main()