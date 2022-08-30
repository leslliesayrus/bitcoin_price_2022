from selenium import webdriver 
from bs4 import BeautifulSoup 
import pandas as pd

# open the site
browser = webdriver.Chrome()
browser.get(f'https://coinmarketcap.com/currencies/bitcoin/historical-data/')

# transform the html text to optimizer the text to BeautifulSoup 
def transform_html(input):
    return " ".join(input.split()).replace('> <', '><')

# web scraping
name_file = 'august'
html = browser.page_source
html = transform_html(html)
page = BeautifulSoup(html, 'html.parser')
table = str(page.findAll('table')[0])
table = pd.read_html(table)
df = table[0]

# processing the data
months = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug"]
number_months = ["01","02","03","04","05","06","07","08"]
for i in range(len(months)):
    df['Date'] = df['Date'].str.replace(f"{months[i]}", f"{number_months[i]}")

df['Date'] = df['Date'].str.replace(",", "")
df['Date'] = df['Date'].str.replace(" ", "-")
df['Open*'] = df['Open*'].str.replace(",", "")
df['Open*'] = df['Open*'].str.replace("$", "")
df['High'] = df['High'].str.replace(",", "")
df['High'] = df['High'].str.replace("$", "")
df['Low'] = df['Low'].str.replace(",", "")
df['Low'] = df['Low'].str.replace("$", "")
df['Close**'] = df['Close**'].str.replace(",", "")
df['Close**'] = df['Close**'].str.replace("$", "")
df['Volume'] = df['Volume'].str.replace(",", "")
df['Volume'] = df['Volume'].str.replace("$", "")
df['Market Cap'] = df['Market Cap'].str.replace(",", "")
df['Market Cap'] = df['Market Cap'].str.replace("$", "")

df.rename(columns={'Open*': 'open'}, inplace = True)
df.rename(columns={'Date': 'date'}, inplace = True)
df.rename(columns={'High': 'high'}, inplace = True)
df.rename(columns={'Low': 'low'}, inplace = True)
df.rename(columns={'Close**': 'close'}, inplace = True)
df.rename(columns={'Volume': 'volume'}, inplace = True)
df.rename(columns={'Market Cap': 'market_cap'}, inplace = True)

df.to_csv(f'{name_file}.csv', index = False)