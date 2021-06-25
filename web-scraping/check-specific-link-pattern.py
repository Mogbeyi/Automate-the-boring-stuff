import requests, sys, webbrowser, bs4, re

res = requests.get(sys.argv[2])

soup = bs4.BeautifulSoup(res.text, "html.parser")

def get_links(pattern):
    link_elems = soup.select('a')
    links = []

    for idx, link in enumerate(soup.find_all('a', href=True)):
        url = link['href']
        if pattern in url: 
            links.append(url)

    return links

def open_links(links):
    for link in links:
        webbrowser.open(link)

def main():
    links = get_links(sys.argv[1])
    open_links(links)

main()

