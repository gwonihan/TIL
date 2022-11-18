import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1&backgroundColor='
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all('li', attrs={'class': re.compile('^search-product')})

# print(items)
# print(items[0].find('div', attrs={'class':'name'}).get_text())

for item in items:
    # 제품명
    name = item.find('div', attrs={'class':'name'}).get_text()
    name = name.split(', ')[0]
    
    # 가격
    price = item.find('strong', attrs={'class':'price-value'}).get_text()
    
    # 평점
    rate = item.find('em', attrs={'class':'rating'})
    if rate :
        rate.get_text()
    else :
        rate = '평점 없음'

    # 리뷰수
    rate_count = item.find('span', attrs={'class':'rating-total-count'})
    if rate_count:
        rate_count.get_text()
    else:
        rate_count = '리뷰수 없음'

    # 광고
    ad = item.find('span', attrs={'class':'ad-badge-text'})
    if ad:
        ad = '광고 있음'
    else:
        ad = '광고 없음'

    # 쿠팡추천
    recommand = item.find('img', attrs={'class': 'badge-ico badge-coupick'})
    if recommand:
        recommand = '쿠팡추천'
    else:
        recommand = '추천 없음'

    print('제품명:', name)
    print('가격:', price)
    print('평점:', rate)
    print('리뷰수:', rate_count)
    print(ad)
    print(recommand)
    print('='*80)