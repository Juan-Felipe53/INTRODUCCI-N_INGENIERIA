try:
    b = float(input("Ingresa la base de tu triangulo: "))
    h = float(input("Ingresa el altura de tu triangulo: "))
    area= (b * h) / 2
    print(f"El área del triangulo es: {area}")
except ValueError:
    print("Ingresa numeros validos")