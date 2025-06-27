def conta_sequencia(sequencia):
    primeiro_numero = sequencia[0]
    subsequencia = []
    contador = 1
    subsequencia.append(primeiro_numero)
    for i, valor in enumerate(sequencia):
        if i > 0:
            if sequencia[i-1] + 1 == valor:
                subsequencia.append(valor)
                contador += 1
                print(subsequencia)
            else:
                contador = 1
                subsequencia.clear()
                subsequencia.append(valor)
    return(print(f'A quantidade de numeros da maior subsequencia da serie é {contador}'))

lista = [1, 9, 3, 10, 4, 20, 2, 11, 12, 13, 14, 15, 17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0]
conta_sequencia(lista)


#  from functools import reduce

# def maximo_minimo(lista):
#     maximo = reduce(lambda a,b: a if a > b else b, lista)
#     minimo = reduce(lambda a,b: a if a < b else b, lista)
#     return maximo, minimo

# print(maximo_minimo([0, 8, 15, 52, 2, 7, 31, 5, 7]))

# def nome_sobrenome(nome_completo):
#     nomes = nome_completo.split(' ')
#     return nomes[-1 ] + ', ' + nomes[0]

# print(nome_sobrenome('Mariucha da Silva'))

# def nome_sobrenome(*nome_completo):
#     print(nome_completo)
#     return nome_completo[-1 ] + ', ' + nome_completo[0]

# print(nome_sobrenome('Mariucha', 'da', 'Silva'))

# from functools import reduce

# numeros = [1, 2, 3, 4, 5]
# numeros_ao_quadrado = list(map(lambda x: x**2, numeros))
# numeros_filtrados = list(filter(lambda x: x%2 == 0, numeros))
# numeros_reduce = int(reduce(lambda a,b: a+b, numeros))
                     
# print(numeros_ao_quadrado)
# print(numeros_filtrados)
# print(numeros_reduce)

#map é tipo um for