from urllib2 import urlopen, HTTPError
from bs4 import BeautifulSoup

source_file = 'file:///Users/mattslight/Dev/5char/input/input5.html'
content = urlopen(source_file)
soup = BeautifulSoup(content, 'lxml')
scrape = soup.findAll('input', attrs={'class': 'linkout'})
for domain in scrape:
    print domain['value'][4:-4]
