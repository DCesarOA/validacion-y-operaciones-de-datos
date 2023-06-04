# Pide los datos necesarios para ejecutar los dos códigos (la frase para saber la longitud y los dos números para encontrar el cuadrante).
frase = input("Ingresa una frase: ")
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

# Programa 1: Longitud de una frase

longitud = len(frase)

# Verifica si el valor de longitud está en el rango de 4 a 8. Si es verdadero, significa que la frase tiene la longitud correcta.
if 4 <= longitud <= 8:
    print("La frase es correcta")
# Verifica si el valor de longitud es menor que 4. Si es verdadero, significa que faltan letras en la frase.
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras")
# Se ejecuta cuando ninguna de las condiciones anteriores es verdadera, lo que significa que la longitud de la frase es mayor que 8.
else:
    print(f"Sobran letras. Tiene {longitud} letras")

# Programa 2: Encuentra el cuadrante

# Verifica la posición de las coordenadas "x" e "y" para determinar si esta en el cuadrante I si ambos son mayores a 0.
if x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I.")
# Verifica la posición de las coordenadas "x" e "y" para determinar si esta en el cuadrante I si "x" es menor a 0 e "y" mayor a 0.
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II.")
# Verifica la posición de las coordenadas "x" e "y" para determinar si esta en el cuadrante I si ambos son menores a 0.
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III.")
# Verifica la posición de las coordenadas "x" e "y" para determinar si esta en el cuadrante I si "x" es mayor a 0 e "y" menor a 0.
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuadrante IV.")
# Si ninguna de las opciones es verdadera quiere decir que ambos numeros son 0 y esta en el origen.
else:
    print("El punto se encuentra en el origen.")