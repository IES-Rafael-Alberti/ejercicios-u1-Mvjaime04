def main():
    correo= input("Ecribe tu correo electronico: ")
    
    separacion=correo.split("@")
    email= separacion[0]
    print("tu correo con nueva extensión es: " + email + "@ceu.es")
if __name__=="__main__":
    main()          