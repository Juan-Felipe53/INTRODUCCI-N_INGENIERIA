import math as mt
try:
    cateto1 = float(input("Ingresa tu cateto a: "))
    cateto2 = float(input("Ingresa tu cateto b: "))
    
    if cateto1 <= 0 or cateto2 <= 0:
        print("Ingresa numeros positivos")
    else: 
        llegar_al = cateto1**2 + cateto2**2
        hipotenusa = mt.sqrt(llegar_al) 
        print(f"La hipotenusa de tu triangulo es: {hipotenusa:.2f}")
except ValueError:
     print("Error: Por favor, ingresa valores numéricos válidos.")