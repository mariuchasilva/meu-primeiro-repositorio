#sintaxe 1: from [nome do arquivo] import [nome da variavel ou funcao], [outra nome de variavel ou funcao, se houver]
#from lista_de_alunos import dados,  nome_do_professor

#sintaxe 2: importando multiplas variaveis de uma vez só
#from lista_de_alunos import *

#sintaxe 3: importanto a biblioteca inteira
import Lista_de_alunos

# importanto arquivos em pastas diferentes
from pasta_qualquer.fizzbuzz import fizz_buzz

# arquivos com variaveis de mesmo nome
# se dados forem iguais, a primeira importação se sobrepõe as demais
# Dica:  posso dar um apelido para a variavel dentro do programa
from Relatorio_do_fundo import dados as dados_dos_fundos

'''
Percorra a lista e exiba o nome, idade e cidade de cada pessoa no formato
João, 25 anos, São Paulo
Maria, 30 anos, Rio de Janeiro
'''
#se e uma lista, posso acessar seus valores atraves do indice
Lista_de_alunos.dados[0]
for dado in Lista_de_alunos.dados:
  # print('\ndado da vez:\n', dado, '\n')
  #se e um dicionario, posso acessar seus valores atraves da chave
  funcionario = ''
  if dado["nome"] is not None:
    funcionario+= dado["nome"]
  if dado["idade"] is not None:
    funcionario = funcionario + ', ' + str(dado["idade"]) + ' anos'
  if dado["endereco"]["cidade"] is not None:
    # print(dado["endereco"]["cidade"])
    funcionario = funcionario + ', ' + dado["endereco"]["cidade"]
  print(funcionario)

  print("O nome do professor e", Lista_de_alunos.nome_do_professor)
  print("O nome da aluna e", Lista_de_alunos.nome_da_aluna)
  print(dados_dos_fundos[2])
   
