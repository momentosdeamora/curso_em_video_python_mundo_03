'''
pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade': 22}
print(pessoas['idade'])
#Na hora de referênciar elementos usa colchetes []. Mas, na hora de declarar usa chaves.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
#del pessoas ['sexo']
pessoas['nome'] = 'Leandro' #Funciona sem precisar dar append
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil) #Lista com dicionários
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #brasil.append(estado[:]) não pode fazer fatiamento
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    '''for v in e.values():
        print(v, end=' ')
    print()'''
    