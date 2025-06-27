# # # rede social
# # amigos_pessoa_1 = ['1235', '987', '0358', '0664']
# # amigos_pessoa_2 = ['07245', '987', '0358', '7487']
# # #como identificar amigos em comum?

# # set_pessoa_1 = set()
# # set_pessoa_2 = set()
# # print(set_pessoa_1)

# # set_pessoa_1.update(amigos_pessoa_1)
# # set_pessoa_2.update(amigos_pessoa_2)
# # print(set_pessoa_1)

# # #intersecao
# # amigos_em_comum = set_pessoa_1.intersection(set_pessoa_2)
# # print("amigos em comum:", amigos_em_comum)

# # #uniao
# # todos_os_amigos = set_pessoa_2.union(set_pessoa_1)
# # print("todos os amigos:", todos_os_amigos)

# #sets nunca terão elementos repetidos

# lista_1 = [2, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 4, 5, 5, 6, 7, 8]
# lista_2 = [2, 4, 5, 3, 5, 6, 7, 8, 9, 9, 4, 5, 5, 6, 7, 8, 0]

# #Qual dessas listas possui menos números repetidos que a outra

# set_lista_1 = set()
# set_lista_2 = set()

# set_lista_1.update(lista_1)
# print(set_lista_1)

# set_lista_2.update(lista_2)
# print(set_lista_2)

# Criando dicionários
# novo_dicionario = {}
# novo_dicionario_2 = dict()

# dicionario_com_elementos = {'chave': 'valor'}
# dicionario_com_elementos_dict = dict(chave_qualquer = 12, outra_chave = False)

#print(dicionario_com_elementos)
#print(dicionario_com_elementos_dict)

# dicionario com lista de tuplas
# dicionario_com_lista_de_tuplas = dict([('aula', 'python'), ('chave_qualquer', 12)])
# print(dicionario_com_lista_de_tuplas)

# dicionario_teste = {'chave_qualquer': 12, 'outra_chave': False, 'nome': 'tanto faz'}
# #print(dicionario_teste)
# # print(len(dicionario_teste))
# # del(dicionario_teste['nome'])
# # # print('nome' not in dicionario_teste)
# # dicionario_teste['nome'] = 'tanto faz'
# # print(dicionario_teste)

# #print('os itens:\n', dicionario_teste.items())
# lista_de_itens = list(dicionario_teste.items())
# print('lista de itens:', lista_de_itens) 
# print('os chaves:\n', dicionario_teste.keys())
# print('os valores:\n', dicionario_teste.values())

# # for x in dicionario_teste:
# #     print(x)

# '''
# os itens:
#   dict_items([('chave_qualquer', 12), ('outra_chave', False), ('nome', 'tanto faz')])
# '''
# #print(dicionario_teste)
# for dict_item in dicionario_teste.items():
#     print(dict_item[0])

# for chave, valor in dicionario_teste.items():
#     print(chave)
#     print(valor)

professor = {
    'nome': 'Lauro',
    'matricula': 123456,
    'alunos': ['jose', 'joao', 'whindersson'],
    'pcd': False,
    'cursos': [
        {
            'curso_id': 'gramatica para devs',
            'periodo': 'noturno',
            'horas-aula': 20,
            'certificado': False
        },
        {
            'curso_id': 'apresentacao de slides',
            'periodo': 'diurno',
            'horas-aula': 10,
            'certificado': True            
        }
    ]
}
#Quantas horas tem o curso gramatica para devs?
#print('lista de itens:', professor.items())

# print(professor['cursos']) lista de dicionarios
# se e uma lista eu posso fazer um for
for curso in professor['cursos']:
    if curso['curso_id'] == 'gramatica para devs':
        print(curso['horas-aula'])

for curso in professor['cursos']:
    if curso['certificado'] == True:
        print(f' O curso {curso['curso_id']} possui certificado')



