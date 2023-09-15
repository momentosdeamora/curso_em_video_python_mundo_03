'''
#Interactive Help
help()
print(input.__doc__)

#Docstrings - String de documentação
""" """ #Começa logo depois do comando def

#Parâmetros opcionais
    def somar(a=0, b=0, c=0)
        s = a + b + c
        print(f'A soma vale(s)')
somar(3, 2, 5)
somar(c=8, b=4)
somar()

#Escopo de Variáveis
def teste():
    x = 8 #Escopo Local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2 #Escopo Global
print(f'No programa principal, n vale {n}')
teste()

#Retornando Valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f' Os resultados foram {r1}, {r2}. {r3}')
'''

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

