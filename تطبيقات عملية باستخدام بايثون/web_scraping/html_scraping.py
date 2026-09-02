import bs4
import requests

headers = {
    'User-Agent': 'Mozilla/5.0'
}

res = requests.get(
    'https://en.wikipedia.org/wiki/Main_Page',
    headers=headers
)


# print(res.text)

nostrachsoup=bs4.BeautifulSoup(res.text,'html.parser')
print(type(nostrachsoup))


el=nostrachsoup.select('#mp-tfa > p')
print(el[0].getText())