import requests, webbrowser
from bs4 import BeautifulSoup as bs
import sys

page_link = sys.argv[1]

r = requests.get(page_link)
soup = bs(r.content, "html.parser")
print(soup)

links = [link["href"] for link in soup.select("src")]

