import bs4

from pathlib import Path

file=open(Path.home()/Path('Desktop','example.html'))
example_soup=bs4.BeautifulSoup(file,'html.parser')
el=example_soup.select('p')
print(el)
print(len(el))
print(el[0].getText())
print(el[0].attrs)
