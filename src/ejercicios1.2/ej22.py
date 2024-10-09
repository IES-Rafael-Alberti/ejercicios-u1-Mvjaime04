def main(): 
    frase=input("Escribe cualquier frase: ")
    vocal=input("Escribe una vocal: ").lower()
    if vocal in "aeiou":
         frase = frase.replace(vocal, vocal.upper())
         print(frase)
        
    else:
        print("error, introduce una vocal")

if __name__=="__main__":
    main()                