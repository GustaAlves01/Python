import requests
from bs4 import BeautifulSoup as bs
from time import sleep

res = requests.get("https://g1.globo.com/")
content = bs(res.content, "html.parser")
noticia = content.find("div", class_="feed-post-body")
titulo = noticia.find("p", elementtiming="text-ssr").text
url = noticia.find("a", class_="feed-post-link gui-color-primary gui-color-hover").text
print(f"titulo: {titulo} aaaa")
print(url)
