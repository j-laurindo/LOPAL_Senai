# Exemplos durante a aula
"""import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"
response = requests.get(url)

print(response.status_code)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

titulos = soup.find_all('div', class_='video-list')

for titulo in titulos:
    print(titulo.text.strip)

with open('titulos.txt','w',encoding='utf-8') as f:
	for titulo in titulos:
		f.write(titulo.text.strip() + '\n')"""

# Exercício

"""import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
agent = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=agent)
response.encoding = 'utf-8    /'
soup = BeautifulSoup(response.text, 'html.parser')

livros = soup.find_all('article', class_='product_pod')

for livro in livros:
	titulo = livro.h3.a['title']
	preco = livro.find('p', class_='price_color').text
	print(f"Nome: {titulo} - Preço: {preco}")"""

# Desafio

import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"
agent = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=agent)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

noticias = soup.find_all('div', class_='feed-post-body')

for noticia in noticias:
    titulos_noticias = noticia.div.h2.p['text-csr']
    link = noticia.a['href']
    print(f"Titulos: {titulos_noticias} - Link: {link}")