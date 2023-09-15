'''num = [2, 5, 9, 1]
num[2] = 3 #Lista é mutavel
num.append(7) #Adicionar novo elemento da lista
num.insert(2, 0) #Adicionar valores. Na posição 2 acrescentar o número 0
num.sort() #Ordenar
num.sort(reverse=True) #Ordenar reverso
num.pop() #Elimina o último valor
num.remove(2) #Procura do inicio da lista a primeira ocorrencia e remove
print(num)
print(f'Essa lista tem{len(num)} elementos.') #conta quantos elementos tem
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')
    print(f'{v}...', end='')'''

'''
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): #pega tanto a chave quanto o valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
'''

'''
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores): #pega tanto a chave quanto o valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
'''

'''
#Python cria uma ligação entre listas a partir do momento em que elas são igualadas
#Ligação

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''

#Copia

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
