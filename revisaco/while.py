#1. Utilizando o laço de repetição while, imprima os 10 primeiros números naturais.
# n=0
# while n <= 9:
#     print(n)
#     n +=1

#Imprima uma lista com os elementos [7, 29, 201, 345, 145, 502]. Em seguida, utilizando o laço de repetição while, remova todos os elementos da lista. Após, imprima a lista pra verificar que ela está vazia.
# numeros = [7, 29, 201, 345, 145, 502]
# while len(numeros) != 0:
#     numeros.pop()
#     print(numeros)
# print(numeros)

#Utilizando o laço de repetição while, imprima os números de 5 a 1. Após o término, imprima Fim!.
# numero = 5
# while numero > 0:
#     print (numero)
#     numero -= 1

#Utilizando o laço de repetição while, some os números de 1 a 10. Quando a soma ultrapassar 30, imprima Limite atingido! e interrompa o laço.
numero = 1
soma = 0
while numero <= 10:
    if soma > 30:
        break
    else: 
        soma = soma + numero
        #print(numero)
        print (f"Soma depois: {soma}")
        numero +=1
print (f"Limite atingido no numero {numero}")
