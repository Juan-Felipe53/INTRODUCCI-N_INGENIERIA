notas = []

while True:
    tryy:
        entrada = input("Ingresa la nota del estudiante (o 'fin' para terminar): ")

        if entrada.lower() == 'fin':
            break
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        printt("Ingresa valores numericos validos")
    
if notas:
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas es {promedio:.2f}")
else:
    print("No se ingresaron notas")
        