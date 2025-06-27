#Após receber uma lista [2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 17, 22, 24, 30],
# Imprima na tela fizz para cada número que for divisível por 3, buzz para cada número divisível
# por 5 e fizzbuzz para cada número divisível por 3 e por 5.

lista = [2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 17, 22, 24, 30]

for item in lista:
    if item % 3 == 0:
        print("buzz")
    elif item % 5 == 0:
        print("buzz")
    elif item % 3 == 0:
        print("fizzbuzz")