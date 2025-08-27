import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


url = 'https://www.dolan-bikes.com/rdx-disc-road/?srsltid=AfmBOor1PrycSOszOmG6gNxoJrgziwnrPeuK6KJCwQDMpxZp-qEgA2Fi'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

table = soup.find('div', class_='responsive-table').find('table')

headers = []
for th in table.find_all('th'):
    headers.append(th.get_text(strip=True))

rows = []

for tr in table.find_all('tr')[1:]:
    cells = []
    for td in tr.find_all('td'):
        cells.append(td.get_text(strip=True))
    rows.append(cells)

df = pd.DataFrame(rows, columns=headers)
df.to_csv('Dolan_RDX_size_table.csv', index=False)