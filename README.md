# Validación y Operaciones de Datos

El codigo se divide en 3 partes

La primera pide los datos al usuario para poder realizar las comprobaciones.
La segunda corre el codigo para verificar la longitus de una frase, con tres opciones, la primera cuando la frase tiene de 4 a 8 letras, la segunda cuando la frase tiene menos de 4 letras y le faltan letras, y la tercera cuando la frase tiene mas de 8 letras y le sobran letras.
La terera corre el codigo para encontrar el cuadrante de las cordenadas con 5 opciones, la pimera comprueba si esta en el cuadrante 1 siendo los dos numeors mayores a 0, la segunda verifica si esta en el cuadrante 2 cuando "x" es menor a 0 e "y" es mayor a 0, la tercera verifica si esta en el cuadrante 3 cuando ambos numeros son menores a 0, la cuarta verifica si esta en el cuadrante 4 si "x" es mayor a 0 e "y" es menor a 0 y por ultimo la quinta cuando ninga de las anteriores es verdadera y quiere decir que ambos numeros son 0, lo que quiere decir que esta en el origen.

Se solicita al usuario que ingrese una frase.
A continuación, se solicita al usuario que ingrese las coordenadas X e Y.

Se calcula la longitud de la frase utilizando la función len(frase).
A continuación, se utilizan estructuras condicionales (if, elif, else) para evaluar diferentes casos:
Si la longitud de la frase está entre 4 y 8 (inclusive), se imprime el mensaje "La frase es correcta".
Si la longitud de la frase es menor que 4, se imprime el mensaje "Hacen falta letras. Solo tiene N letras", donde N es la longitud de la frase.
Si la longitud de la frase es mayor que 8, se imprime el mensaje "Sobran letras. Tiene N letras", donde N es la longitud de la frase.


Se utilizan nuevamente estructuras condicionales para evaluar las coordenadas y determinar en qué cuadrante se encuentra el punto representado por esas coordenadas:
Si tanto X como Y son mayores que 0, el punto se encuentra en el cuadrante I.
Si X es menor que 0 y Y es mayor que 0, el punto se encuentra en el cuadrante II.
Si tanto X como Y son menores que 0, el punto se encuentra en el cuadrante III.
Si X es mayor que 0 y Y es menor que 0, el punto se encuentra en el cuadrante IV.
Si ninguna de las condiciones anteriores se cumple, esto significa que ambas coordenadas son iguales a 0, por lo que el punto se encuentra en el origen.
Se imprime el mensaje correspondiente al cuadrante en el que se encuentra el punto.