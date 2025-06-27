def ola_x(x):
    return 'ola' + x

variavel_qualquer = ola_x('teste')


minha_variavel = lambda x: 'ola ' + x if x == 'teste' else 'tchau'
print(minha_variavel())

# def calcular_media(*notas, arredondar=False):
#     media = sum(notas) / len(notas)
#     if arredondar:
#         return round(media)
#     return media

# print(calcular_media(7.5, 8.0, 6.5))
# print(calcular_media(7.5, 8.0, 6.5, arredondar=True))

# funcao_com_kwargs(numero=8, lista=['um item', 'dois itens'], booleano=False)
# def funcao_com_kwargs(**kwargs):
#     print('*kwargs:', kwargs)
#     for chave, valor in kwargs.items():
#         print('chave', chave, 'valor', valor)

# funcao_com_kwargs(numero=8, lista=['um item', 'dois itens'], booleano=False)

# def funcao_com_args(*args):
#     print('*args:', args)
#     for item in args:
#         print(item)

# funcao_com_args(1, 5, 'teste', False, None, ['lista'], {'chave', 'valor'})


# def soma(a,b):
#     return a + b

# def calculadora(a, b, operacao):
#     if operacao == 'soma':
#         return soma(a,b)
#     elif operacao == 'multiplicacao':
#         return a * b
#     elif operacao == 'potencia':
#         return a ** b
#     else:
#         return 'Operacao Invalida'

# print(calculadora(3, 4, 'soma'))
# print(calculadora(3, 4, 'multiplicacao'))
# print(calculadora(3, 4, 'potencia'))



# def converte_em_dolar(valor):
#     cotacao_do_dolar = 10
#     valor_convertido = valor * cotacao_do_dolar
#     return f'Fazendo a conversao, fica em {valor_convertido}'


# def mae_e_filha(mae, filha):
#     return f'{mae} e mae de {filha}'

# print(mae_e_filha("Fernanda Torres", 'Fernanda Montenegro'))