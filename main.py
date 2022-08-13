import requests
import bs4
from keywords import KEYWORDS
HEADERS = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding':'gzip, deflate, br',
           'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'Cache-Control':'max-age=0',
           'Connection':'keep-alive',
           'Cookie':'_ym_uid=1652613936790676754; _ym_d=1652613936; _ga=GA1.2.92592192.1652613936; hl=ru; fl=ru; habr_web_home_feed=/all/; _ym_isad=2; visited_articles=682250:472258:324982',
           'Host':'habr.com',
           'Referer':'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
           'sec-ch-ua':'"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
           'sec-ch-ua-mobile':'?0',
           'sec-ch-ua-platform': "Windows",
           'Sec-Fetch-Dest':'document',
           'Sec-Fetch-Mode':'navigate',
           'Sec-Fetch-Site':'same-origin',
           'Sec-Fetch-User':'?1',
           'Upgrade-Insecure-Requests':'1',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83 (Edition Yx)'
           }

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = {hub.find('a').text.strip() for hub in hubs}
    if hubs & KEYWORDS:
        article_time = article.find('time').attrs['title']
        article_name = article.find('h2').find('a')
        article_url = 'https://habr.com' + article.find('h2').find('a').attrs['href']
        print(article_time,'//',article_name.text,' ---> ',article_url)

