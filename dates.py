import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.fool.com/investing/top-stocks-to-buy.aspx').read()
soup= bs.BeautifulSoup(sauce, 'lxml')
print(soup)

