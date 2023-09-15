'''def soma(a, b):
    s = a + b
    print(s)


#Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=7, a=2)'''

'''def contador(* num):
    for valor in num:
        print(valor, end='')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''
#LISTA
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''

'''
#DESEMPACOTAR *

def soma(* valores):
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    
soma(5, 2)
soma(2, 9, 4)
'''