import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.foxsports.com/soccer/aston-villa-team-schedule').read()
soup= bs.BeautifulSoup(sauce, 'lxml')
print(soup)
