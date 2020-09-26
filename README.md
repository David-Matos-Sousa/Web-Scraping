# :space_invader: Web Scraping :man_technologist:

## Tarefas:
- [x] Mergulhar nos conceitos 
- [x] Entender ferramentas
- [x] Fazer alguns exemplos
- [ ] Desenvolver um projeto próprio 

## **Definições:**

**Web scraping** -> Sucintamente é a extração e manipulação de dados em sites. Web scraping é utilizado em muitos processos de automatização de tarefas, pois por meio do navegador ou de requests em sites obtêm acesso às informações contidas neles.

**Fetching** -> Baixar o conteúdo da página

**Parsing** -> Analise do conteúdo HTML da página 

**Requests** -> Biblioteca Python para fazer requisições a sites

**BeautifulSoup** -> Biblioteca Python de extração de dados de arquivos HTML e XML

## **Exemplos:**
- [Script que extrai todos os fornecedores de um site e retorna um arquivo csv :trophy: | BeautifulSoup, Requests](https://github.com/David-Matos-Sousa/Web-Scraping/blob/master/main.py) 
- [Script que retorna alguns rankings da NBA em um arquivo json :basketball: | Selenium, BeautifulSoup, Requests](https://github.com/David-Matos-Sousa/Web-Scraping/blob/master/Exemplo_02.py)
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
