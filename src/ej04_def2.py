def grados_celsius(f:float) -> float :
    c = (f-32)*5/9
    return c

def main():
    f=float(input ("dame una temperatura en grados Fahrenheit: "))


    celsius=grados_celsius(f)

    print(f"tu temperatura es la siguiente: {celsius:.2f}ºC ({f:.2f}ºF)")
if __name__=="__main__":
    main()