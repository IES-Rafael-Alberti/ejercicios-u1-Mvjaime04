pan= 3.49 
dia_despues= pan*0.60
dia=int(input("introduce las barras no frescas vendidas: "))
precio_dia=dia*dia_despues
print(f"el coste habitual de la barra es de {pan} €")
print(f"el precio con descuento de una barra no fresca es de {dia_despues} € ")
print("el precio con descuento final de todas las barras no frescas es de {} €".format(precio_dia))