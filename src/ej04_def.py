def grados_celsius(cº,fahrenheit):
    return(f"tu temperatura es la siguiente: {cº}ºC ({fahrenheit}ºF)")

def main():
    f=int(input("dame una temperatura en grados Fahrenheit: "))

    celsius= (f-32)*5/9
    resultado=grados_celsius(celsius,f)

    print(resultado)
if __name__=="__main__":
    main()
