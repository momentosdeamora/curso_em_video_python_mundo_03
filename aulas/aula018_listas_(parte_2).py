'''teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste)
print(galera)'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste) #Criando uma ligação entre as duas estruturas. Se eu mudo uma, eu mudo as duas.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade')'''

'''galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)'''

galera = list()
dado = list()
totmai = totmen = 0 #Pode fazer com variaveis simples mas não pode fazer com as compostas
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
