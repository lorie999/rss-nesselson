import cloudscraper
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
import time

URL = "https://www.rogerebert.com/contributors/lisa-nesselson"

print("Descarregant la pagina...")
scraper = cloudscraper.create_scraper()
resposta = scraper.get(URL)

if resposta.status_code != 200:
    print(f"Error: codi {resposta.status_code}")
    exit()

print("Pagina descarregada correctament")
sopa = BeautifulSoup(resposta.text, "html.parser")

fg = FeedGenerator()
fg.title("Lisa Nesselson - RogerEbert.com")
fg.link(href=URL)
fg.description("Articles de Lisa Nesselson a RogerEbert.com")

articles = sopa.find_all("article")

if not articles:
    print("No s'han trobat articles.")
else:
    print(f"Trobats {len(articles)} articles")

for article in articles:
    titol_tag = article.find("h2") or article.find("h3") or article.find("a")
    link_tag = article.find("a", href=True)

    if titol_tag and link_tag:
        titol = titol_tag.get_text(strip=True)
        link = link_tag["href"]

        if link.startswith("/"):
            link = "https://www.rogerebert.com" + link

        imatge_url = ""
        try:
            resposta_a
