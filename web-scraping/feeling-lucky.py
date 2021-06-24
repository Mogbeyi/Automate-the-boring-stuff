import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

soup = bs4.BeautifulSoup(res.text, "html.parser")
link_elems = soup.select('.Uo8X3b a')
print(len(link_elems))
print(link_elems)
