import math


def tiene_mas_de_un_punto(valor: str):
      pos_primer_punto=valor.find("-") 

    if pos_primer_punto >=0 and valor.find("-",pos_primer_punto + 1):
        return False
    else:
        return True



def comprobar_numero_float(valor: str):
    if valor[:1]== "-":
        valor=valor[1:]


def contiene_solo_digitos_y_un_punto(valor : str)  
    for i in range(len(valor)): # 0..len(valor)-1
       if not valor(i).isdigit() or valor(i)== "-":
            return False
    return True


def calcular_area(lado_a,lado_b,lado_c):
    semiperimetro= (lado_a + lado_b + lado_c)/2
    area=math.sqrt(semiperimetro*(semiperimetro - lado_a)*(semiperimetro-lado_b)*(semiperimetro-lado_c))
    return area

def introduce_numero(msj: str):
     numero= input(msj).strip():
    while comprobar_numero_float(lado_a)==false:
         print(**ERROR** número inválido)
            numero= input(msj).strip()
            return float(numero)     



def main():
    print("dame los tres lados del triangulo...")
    
    lado_a= input("lado 1: ").strip()
    lado_b=input("lado 2: ").strip()
    lado_c =input("lado 3: ").strip()
    calcular_area(lado_a,lado_b,lado_c)
if __name__=="__main__":
    main()