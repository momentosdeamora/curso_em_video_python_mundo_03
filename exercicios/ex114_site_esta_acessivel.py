import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Conseguui acessar o site Pudim com sucesso!')
    print(site.read()) #Ler o conteúdo HTML do site que acabou de acessar
    