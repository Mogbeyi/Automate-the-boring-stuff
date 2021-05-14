import requests

class Request(object):

	def __init__(self, url):
		self.url = url

	def get_text(self):
		return requests.get(self.url)

class File(object):

	def __init__(self, filename):
		self.filename = filename

	def write(self, data):
		with open(self.filename, 'w') as f:
			f.write(data.text[:500])

	def read(self):
		with open(self.filename, 'r') as f:
			for line in f:
				print(line)

def main():
	request = Request('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
	text = request.get_text()
	file = File('gutenberg.txt')
	file.write(text)
	file.read()

main()


