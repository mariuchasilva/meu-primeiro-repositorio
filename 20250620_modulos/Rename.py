'''
criando um programa que renomeia nossos arquivos, conecando com letra maiuscula

'''

import os
from pathlib import Path
minha_pasta = Path("C:/Users/Mari/Documents/Una/meus-projetos/meu-primeiro-repositorio/20250620_modulos")

def renomear_arquivos(diretorio):
    #print('diretorio:', diretorio)
    #print('\ndiretorio usando os:\n', os.listdir(diretorio), '\n')
    for conteudo_da_pasta in os.listdir(diretorio):
        #print('\narquivo:\n', os.path.join(diretorio, conteudo_da_pasta))
        if os.path.isfile(os.path.join(diretorio, conteudo_da_pasta)):
            #print(conteudo_da_pasta + ' e um arquivo')
            novo_nome = conteudo_da_pasta[0].upper() + conteudo_da_pasta[1:]
            print("novo nome depois da conversao", novo_nome)
            caminho_nome_antigo = os.path.join(diretorio, conteudo_da_pasta)
            caminho_nome_novo = os.path.join(diretorio, novo_nome)
            os.rename(caminho_nome_antigo, caminho_nome_novo)

renomear_arquivos(minha_pasta)