
 
def comprobar_entero(cadena:str) -> bool :
   cadena = cadena.strip()
   return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit) 
   


 
def dame_entero() -> int:
   cadena=input("dame un entero")
   while not comprobar_entero(cadena):
      cadena = input("\n**Error** no es un entero!!!\n\n Dame un numero de verdad:")

   return int(cadena)


 
 


def main():
 num= dame_entero
 print("Escribiste el número {}".format(num))



if __name__=="main":
 main()