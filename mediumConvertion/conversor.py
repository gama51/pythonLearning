menu= """
Welcome to coin converter 🍕

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opción: 
"""
option=input(menu)

if option=="1":
        
        pesos = input("How much Colombian pesos do you have?: ")
        pesos = float(pesos)
        valor_dolar=3875
        dolares=round(pesos/valor_dolar,2)
        dolares=str(dolares)
        print("you have $ "+dolares+" Dolares")    
elif option=="2":
        pesos = input("How much Argentinians pesos do you have? ")
        pesos = float(pesos)
        valor_dolar=65
        dolares=round(pesos/valor_dolar,2)
        dolares=str(dolares)
        print("You have $ "+dolares+" Dolares") 
elif option=="3":
        pesos = input("How much Mexican pesos do you have? ")
        pesos = float(pesos)
        valor_dolar=24
        dolares=round(pesos/valor_dolar,2)
        dolares=str(dolares)
        print("You have $ "+dolares+" Dolares")   
else:
    print("Plese type a rigth option")


