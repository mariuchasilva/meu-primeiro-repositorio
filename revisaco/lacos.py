'''
sintaxe de um laço de repetição for:
for [nome que quiser] in [variavel lista]:
    --> execute um comando para cada item
'''
# contratos = [100, 125, 156, 175, 200, 300]
# contador_de_contratos = 0
# for contrato in contratos:
#     contador_de_contratos +=1
#     if contrato > 150:
#         print(f'o contrato {contrato} vale mais que 150')
#     else:
#         print(f'o contrato {contrato} vale menos ou igual a 150')

#print(f'o total de contratos maiores que 150 e {contador_de_contratos}')
#print ('fim do codigo')

'''
crie um contador que imprimira "Lancar" após 5 intervalos de tempo
'''
# contador = 5

# while contador > 0:
#     #print(f'Contagem regressiva: {contador}')
#     contador -=1
# #print('Lancar')

contratos = [100, 125, 156, 175, 200, 300]

meta = 500
total = 0
indice = 0

while indice < len(contratos) and total < meta:
    total += contratos[indice]
    print(f"Contrato {indice+1}: R${contratos[indice]} | Total parcial: R${total}")
    indice += 1

print(f"\nMeta {'atingida' if total >= meta else 'nao atingida'}")
print(f"Total: R${total}")

#while --> olha para a condição
#for --> olha para todos os itens da lista