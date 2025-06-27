#cadastro de novo fundo na base de dados
# nome_do_fundo = "Learn Python"
# tipo_de_fundo = "multimercado"
# isento_de_IR = True
# investimento_minimo = 5000

# nome_do_outro_fundo = "build python app"
# tipo_de_outro_fundo = "renda fixa"
# isento_de_IR_outro_fundo = False
# investimento_minimo_outro_fundo = 1000
# rating = 'AAA'

#de volta a fila de ingressos
primeira_pessoa = 'Felipe'
segunda_pessoa = 'Victor'
terceira_pessoa = 'Renata'

# qual foi a forma de pagamento?
# pagou meia entrada ou inteira?
# o ingresso foi cortesia?

primeira_pessoa_pagamento = 'credito'
primeira_pessoa_meia_entrada = False
primeira_pessoa_foi_cortesia = False
primeira_pessoa_acompanhante = ['Marcia', 'Bruno', 'zeca']
primeira_pessoa_cupom_sorteio = 7987
fila_de_ingressos = []

#varios append depois
fila_ingressos = ['credito', False, False, ['Marcia', 'Bruno', 'zeca'], 7987]

#lista armazena dados do mesmo tipo (mesma classe)

fundo_python = {
    'nome_do_fundo': 'Learn Python',
    'tipo_de_fundo': 'multimercado',
    'isento_de_IR': True,
    'investimento_minimo': 5000,
}
#print(fundo_python)

ingresso_felipe = {
    'nome': 'felipe',
    'meia_entrada': False,
    'acompanhantes': ['Marcia', 'Bruno', 'zeca'],
    'codigo_compra': 7987
}
print(ingresso_felipe['meia_entrada'])
print(ingresso_felipe.get('nome'))

print(ingresso_felipe['acompanhantes'][0])
print(ingresso_felipe.get('acompanhantes')[0])

fundo_python['investimento_minimo']=1000

print(fundo_python)
