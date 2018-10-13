from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Computer_science"
page = urlopen(url)
soup = BeautifulSoup(page)
print ("title:", soup.title.string)
print(soup.find('table', class_='wikitable sortable plainrowheaders'))
