import requests
from bs4 import BeautifulSoup

'''
Creates a table to decode country codes from wikipedia
'''

url = 'https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

decoderDict = {}
table = soup.find('table', {'class':'wikitable sortable sort-under'}) #table containing rows of country codes and names
rows = table.findAll('tr') #each row within the table

for row in rows[1:]: #traverse each row in the table starting from the first row
    cells = row.findAll('td') #each cell in the row
    code = cells[0].text 
    countryName = cells[1].text
    decoderDict[code] = countryName #assign values in dictionary
