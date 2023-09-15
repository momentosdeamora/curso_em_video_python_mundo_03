# lanche = ()tupla []lista {}dicionário
# ignora o último elemento
'''
lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[3])

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3])

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:])

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3:])'''

'''
lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
Tuplas são imutáveis
lanche[1] = 'Refrigerante'
print(lanche)
'''

#Mesmo resultado

'''
lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos})
print('Comi pra caramba!')
'''

'''
lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')
'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) #colocar em ordem'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8)) #mostra a posição que o número está
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(5,1))
'''

'''
#pode ter dados diferentes dentro da tupla
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) #Tupla é imutavel, menos para ser apagada. Pode deletar a tupla inteira menos o elemento individualmente
print(pessoa)
'''