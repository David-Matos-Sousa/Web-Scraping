# :space_invader: Web Scraping :man_technologist:

## Tarefas:
- [x] Mergulhar nos conceitos 
- [x] Entender ferramentas
- [x] Fazer alguns exemplos
- [ ] Desenvolver um projeto próprio 

## **Definições:**

**Web scraping** -> Basicamente é a extração e manipulação de dados em sites. Web Scraping é utilizado em muitos processos de automatização de tarefas, pois por meio do navegador ou de requests em sites é possível obter acesso às informações contidas no HTML. Esses dados podem ser manipulados, organizados e transformados de acordo com a sua necessidade. Existem muitas possibilidades que você pode explorar o Web Scraping para realizar um projeto, um exemplo seria para criar um script para visualizar os dados de um site e retornar em um arquivo csv, pegar as informações dos sites de viagem e ver qual a passagem mais barata para um determinado destino, entre outros muitos usos diversificados da ferramenta.

**Fetching** -> Buscar os dados de uma página por meio do script.

**Parsing** -> É o processo de análise do conteúdo da página em HTML e organização do mesmo por meio de tags, divs e etc.

**Requests** -> Biblioteca Python utilizada para fazer requisições a sites em HTTP, de modo a acessar o conteúdo do site.

**BeautifulSoup** -> Biblioteca Python que faz a extração, manipulação e o parseamento do dados em HTML e XML.

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
