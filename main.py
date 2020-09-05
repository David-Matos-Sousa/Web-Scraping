import requests # Utilizei para acessar o site e pegar as informações posteriormente
import csv # Utilizei para poder criar o arquivo csv com os dados que vou extrair do site
from bs4 import BeautifulSoup # Utilizei para poder pegar as informações 

csv_file = open('fornecedores.csv','w', newline='') # Criar um novo arquivo csv editável
csv_writter = csv.writer(csv_file) # Criação da variável para escrever no arquivo csv
csv_writter.writerow(['empresa','responsavel','telefone','site']) # Criação do cabeçalho do csv

url = 'https://www.abimad.com.br/associados/pesquisar#menu-top'
r = requests.get(url) # Criação da variável r que faz a requisição pro site

soup = BeautifulSoup(r.content, 'html.parser')  # Criação do objeto Soup; Puxando o conteúdo do site; Organizando (Parseando) esse conteúdo em html.

informacoes = soup.find_all('figure') # Atribuição dos retornos da classe figure à variavel

#Como a BeaultifulSoup sempre puxa o primeiro elemento, é necessário fazer um for para pegar outros dados da página

for fornecedor in informacoes: # for para pegar os dados desejados

  empresa = fornecedor.h5.text # Pegando o texto do h5 que é o nome da empresa

  responsavel = fornecedor.find('i', class_= 'fa-user').next_element.next_element.text # Para achar o nome do responsavel utilizar o next element depois de achar a classe que ele pertence e puxar o texto com o .text

  phone = fornecedor.find('i', class_= 'fa-phone').next_element.next_element.text # Para achar o telefone da empresa utilizar o next element depois de achar a classe que ele pertence e puxar o texto com o .text

  site = fornecedor.find('i', class_ ='fa-link').next_element.next_element.text # Para achar o site da empresa utilizar o next element depois de achar a classe que ele pertence e puxar o texto com o .text

  print('Empresa:{}'.format(empresa))
  print('Responsavel: {}'.format(responsavel))
  print('Phone: {}'.format(phone))
  print('Site: {}'.format(site))
  print('-'*20)

  # Print's para visualizar as informações

  csv_writter.writerow([empresa, responsavel,phone,site]) # Para escrever nas linhas do csv os dados retirados do site

csv_file.close(0) ## fecha o arquivo csv

# Estava com bastante dificuldade de fazer um código que retornasse algo pra além do [] em Web Scraping e fiquei muito feliz ao conseguir terminar esse =D
# Aprendi tudo isso com esse vídeo aqui:  
# https://www.youtube.com/watch?v=anv-Vt_FL4E
# Até a próxima! 
