# pessoas = ['felipe', 'victor','renata']
# pessoas.append('bruno')
# print(pessoas)

# #criando uma tupla
# numeros = (90, 11, 25, 11, 88, 74)
# #contando quantas vezes aparece o número 11 na tupla
# print(numeros.count(11))

# #criando lista
# lista = [10, 21, 32, 43]

# lista.append(54)
# print (lista)

# lista.insert(3,99)
# print (lista)

# lista.remove(32)
# print(lista)

# #retira o último elemento para uma outra lista
# ultimo_elemento = lista.pop()
# print(lista)
# print(ultimo_elemento)

# indice = lista.index(99)
# print(indice)

# lista = [10, 20, 30, 40, 50]

# if 30 in lista:
#     print("O numero 30 esta na lista")
# else:
#     print("O numero 30 não esta na lista")

"""
Exercícios Lauro
"""
#Crie uma lista com as strings 'infinity', 'school', 'curso', 'dfs'.

lista = ['infinity', 'school', 'curso', 'dfs']
print(lista)

#Insira a string 'python' na lista do exercício acima.
lista.append('python')
print(lista)

#Imprima a lista após remover o primeiro elemento dela.

lista.remove('infinity')
print(lista)

#Imprima a lista após remover o último elemento dela.
print(lista[-1])
del lista[-1]
print(lista)

#Defina que o terceiro elemento da lista será 'course' e imprima a lista.
print(lista[2])
lista[2] = 'course'
print(lista)

#Com a lista ['Mike', '', 'Emma', 'Kelly', '', 'Brad'], imprima a lista sem as strings vazias.
lista_2 = ['Mike', '', 'Emma', 'Kelly', '', 'Brad']
print(lista_2)
lista_3 = [i for i in lista_2 if i != '']
print(lista_3)