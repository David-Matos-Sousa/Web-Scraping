# :space_invader: Web Scraping :man_technologist:
 Aprendendo Web Scraping.

## Tarefas:
- [x] Mergulhar nos conceitos 
- [ ] Entender ferramentas
- [ ] Fazer alguns exemplos
- [ ] Desenvolver um projeto próprio 


**Web scraping** -> Extração de dados em sites

**Fetching** -> Baixar o conteúdo da página

**Parsing** -> Analise do conteúdo HTML da página 

**Requests** -> Requisições a sites

**Beautiful Soup** -> Biblioteca Python de extração de dados de arquivos HTML e XML.

### **Comandos:**
***
 `from bs4 import BeautifulSoup` -> Usado para importar a biblioteca
 
`soup = BeautifulSoup(html_doc, 'html.parser')` -> Cria um objeto soup com a estrutura de dados aninhada

`print(soup.prettify())` -> Mostra como as tags estão aninhadas no documento

`soup.find_all('a')` -> Procura no site o conteúdo dentro do ''

`soup.find(id="link3")` -> Procura no site o id informado

`soup.find(class="fyi")` -> Procura no site a classe informada

`print(soup.get_text())` -> Extrai todo o texto do site





**Fontes**: https://en.wikipedia.org/wiki/Web_scraping; https://en.wikipedia.org/wiki/Data_scraping; https://en.wikipedia.org/wiki/Data_scraping; https://www.crummy.com/software/BeautifulSoup/bs4/doc/; 
