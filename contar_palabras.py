contar_palabras = input("Ingresa una frase para contar sus palabras: ")
frase = contar_palabras.split()
count = 0
for palabra in frase:
    count +=1
print(f"La cantidad de palabras que tiene tu frase son: {count}")

