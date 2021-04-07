import re
import requests, webbrowser
from bs4 import BeautifulSoup as bs

r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup = bs(r.content, "html.parser")

#
# headers = soup.find_all(['h2', 'h1'])
# links = soup.find('a')
#
# for header in headers:
#    print(header.text)
#
# print(links['href'])
#webbrowser.open(links['href'])
#
# headers = soup.find_all('h2', string=re.compile("(H|h)eader"))
# print(headers)
# content = soup.select('div p')
# print(content)
#

links = soup.select("ul.socials a")
actual_links = [link["href"] for link in links]
fun_facts = soup.select("ul.fun-facts")
fun_facts_text = [fun_fact.text.replace("\n", ",") for fun_fact in fun_facts]
print(fun_facts_text)
print(len(fun_facts_text))
