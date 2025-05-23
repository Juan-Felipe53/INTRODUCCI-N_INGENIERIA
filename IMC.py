peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

IMC = peso / altura ** 2

if IMC < 18.5:
    print("Tienes un peso muy bajo")
elif 18.5 <= IMC < 24.9:
    print("Estas en un peso normal")
elif 25 <=  IMC < 29.9:
    print("Estas en sobrepeso")
else:
    print("Estas en estado de obesidad")
