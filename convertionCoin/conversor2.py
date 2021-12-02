dolares = input("¿Cúantos USD tienes?: ")
dolares = float(dolares)
valor_dolar=3946.90
pesos=round(valor_dolar*dolares,2)
pesos=str(pesos)
print("Tienes $ "+pesos+" COP")