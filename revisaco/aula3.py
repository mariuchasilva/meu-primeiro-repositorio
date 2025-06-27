#Desafios maiores
#3
# lista = ['classe', 'objeto', 'dicionário', 'tupla', 'lista']
# lista_2 = []
# for item in lista:
#     lista_2 = item.capitalize()
#     print(lista_2)

#4
# tupla = ('Orange', [10, 20, 30], (5, 15, 25))
# print(tupla[1][2])

#5
lista_de_dicionarios = [
        {"nome": "Alice", "idade": 25},
        {"nome": "Bob", "idade": 30},
]

#print(lista_de_dicionarios[0])

lista_nomes = []

for item in lista_de_dicionarios:
    print(f'item:  {item}, {lista_nomes}')
    lista_nomes = item['nome']

    
