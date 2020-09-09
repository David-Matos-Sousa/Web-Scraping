# :space_invader: Web Scraping :man_technologist:

## Tarefas:
- [x] Mergulhar nos conceitos 
- [x] Entender ferramentas
- [x] Fazer alguns exemplos
- [ ] Desenvolver um projeto próprio 

## **Definições:**

**Web scraping** -> Extração de dados em sites

**Fetching** -> Baixar o conteúdo da página

**Parsing** -> Analise do conteúdo HTML da página 

**Requests** -> Biblioteca Python para fazer requisições a sites

**Beautiful Soup** -> Biblioteca Python de extração de dados de arquivos HTML e XML

## **Exemplos:**
- 
- 
### **Comandos:**
***
 `from bs4 import BeautifulSoup` -> Usado para importar a biblioteca
 
`soup = BeautifulSoup(html_doc, 'html.parser')` -> Cria um objeto soup com a estrutura de dados parseada (alinhada/organizada)

`soup.prettify()` -> Mostra como as tags estão aninhadas no documento

`soup.find_all('a')` -> Procura no site o conteúdo dentro do ''

`soup.find(id="link3")` -> Procura no site o id informado

`soup.find(class="fyi")` -> Procura no site a classe informada

`soup.get_text()` -> Extrai todo o texto do site

`soup.find('div', class_= 'small-widget').h2` -> Retorna o h2 da classe informada

`soup.find('i', class_ ='fa-link').next_element.next_element` -> Retorna o próximo elemento (quantas vezes for digitado)

`soup.find('i', class_ ='fa-link').next_element.text`-> Pega o texto do próximo elemento

`for fornecedor in informacoes:
  responsavel = fornecedor.find('i', class_= 'fa-user').next_element.next_element.text` -> Como a BeaultifulSoup sempre puxa o primeiro elemento, é necessário fazer um for para pegar outros dados da página 

## **Referências**: 
- **Artigo na Wikipedia sobre Web Scraping (Inglês)** | https://en.wikipedia.org/wiki/Web_scraping
- **Artigo na Wikipedia sobre Data Scraping (Inglês)** | https://en.wikipedia.org/wiki/Data_scraping 
- **Documentação da BeautifulSoup (Inglês)** | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
- **Documentação da BeautifulSoup (Português)** | https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
- **Video tutorial sobre sobre Web Scraping e BeautifulSoup (Português)** | https://www.youtube.com/watch?v=anv-Vt_FL4E
