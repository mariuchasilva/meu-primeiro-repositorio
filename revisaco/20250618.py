# '''
# verifica se e palindromo
# '''

# def palindromo(palavra, outra_palavra):
#     lista_palavra = list(palavra)
#     lista_outra_palavra = list(outra_palavra)
#     if len(lista_palavra) != len(lista_outra_palavra):
#         print('Nao e palindromo')
#         return
#     lista_outra_palavra.reverse()
#     print(lista_outra_palavra)

#     palavra_de_novo = ''.join(lista_palavra)
#     outra_palavra_de_novo = ''.join(lista_outra_palavra)

#     print(palavra_de_novo, outra_palavra_de_novo)

#     return palavra_de_novo == outra_palavra_de_novo
# palindromo('tebet', 'tabet')

#Removendo o ultimo par chave-valor inserido

# dicionario =  {'a':10,'b':20,'c':30,'d':40,'e':50}
# ultima_chave, ultimo_valor = dicionario.popitem()
# print(dicionario)
# print(type(ultima_chave), type(ultimo_valor))

# dicionario =  {'a':10,'b':20,'c':30,'d':40,'e':50}
# tupla = dicionario.popitem()
# print(dicionario)
# print(tupla)

# dicionario = {'arroz': 10, 'feijao': 20, 'macarrao': 15}

# chaves = list(dicionario.keys())
# print(chaves)
# i= 0 
# while i < len(chaves):
#     chave = chaves[i]
#     print(f'O preco de {chave} e {dicionario}')
#     i += 1

def max_min(lista):
    max = lista[0]
    min = lista[0]
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
        if lista[i] < min:
            min = lista[i]
    return (print(max), print(min))

lista = [1, 12, 25, 2, 13, -9, 35]
max_min(lista)

def agrupa_strings(*args):
    dicionario = {}
    for palavra in args:
        chave = palavra[0]
        valor = palavra
        if chave not in dicionario:
            dicionario[chave] = [valor]
        else:
            dicionario[chave].append(palavra)
    return(print(dicionario))

agrupa_strings('carro', 'escola', 'aviao', 'bombeiro', 'piscina', 'vaca', 'lapis', 'azul', 'violao', 'boicote')

