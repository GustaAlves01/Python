import requests
from bs4 import BeautifulSoup as bs


for pagina in range(1,51):
	site = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
	res = requests.get(site, timeout=10)

	if (res.status_code == 200):
		content = bs(res.content, "html.parser")
		livros = content.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

		for livro in livros:
			titulo = livro.find("h3").text
			preco = livro.find("p", class_="price_color").text
			estoque = livro.find("p", class_="instock availability").text.strip()
			estoque = "disponivel" if "In stock" in estoque else "indisponivel"
			print(f"titulo: {titulo} \n"+
			f"preco: {preco}\n"+
			f"estoque: {estoque}")
			print("-"*10)

		print("="*10
                 + f"\n pagina {pagina}\n"
                 + "="*10)

	else:
		print("Nao conectado")
