import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

decoderDict = {}
table = soup.find('table', {'class':'wikitable sortable sort-under'})
rows = table.findAll('tr')

for row in rows[1:]:
    cells = row.findAll('td')
    code = cells[0].text
    countryName = cells[1].text
    decoderDict[code] = countryName
