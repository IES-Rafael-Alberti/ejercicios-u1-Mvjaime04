def main():
    num1=int(input("Dame un número inicial: "))
    num2=int(input("dame un segundo número: ")) 

    if num1==num2:
        print("Los números introducidos no pueden ser iguales")

    if num1>num2:
     menor=num2
     mayor=num1
    else:
        menor=num1
        mayor=num2

    cuenta=mayor-menor 

    print(f"el número menor es {menor} y entre ellos existe {cuenta} ")
if __name__=="__main__":
   main()

