import requests
from bs4 import BeautifulSoup as bs

def main():
    for page in range(1,51):
        site = f"https://books.toscrape.com/catalogue/page-{page}.html"
        res = requests.get(site)
        conection = res.status_code == 200
        
        if conection:
            content = bs(res.content, "html.parser")
            book_data(content, page)   

        else:
            print(f"conection failed at page {page}")
            continue


def book_data(content, page):
    books = content.find_all("article", class_ = "product_pod")

    for book in books:

        book_dicionary = {
            "title": book.find("h3").find("a")['title'],
            "price": book.find("p", class_="price_color").text,
            "stock": book.find("p", class_="instock availability").text.strip()
        }
        print(f"title: {book_dicionary['title']}\n"+
              f"price: {book_dicionary['price']}\n"+
              f"stock: {book_dicionary['stock']}\n"+
              "-"*10)

    print (f"page: {page}")    

if __name__ == "__main__":
    main()
