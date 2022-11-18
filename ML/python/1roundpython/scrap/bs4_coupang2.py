import requests
from bs4 import BeautifulSoup
import re

for i in range(1, 6):

    # url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor='
    url = f'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={1}&rocketAll=false&searchIndexingToken=1&backgroundColor='
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    # print(len(soup.text))


    items = soup.find_all('li', attrs={'class': re.compile('^search-product')})

    # print(items)
    # print(items[0].find('div', attrs={'class':'name'}).get_text())
    for item in items:
        # 제품명
        name = item.find('div', attrs={'class':'name'}).get_text()

        badge = item.find('img', attrs={'class':"badge-ico badge-coupick"})
        if badge:
            print('쿠팡 추천 제품 제외!!')
            print('='*80)
            continue

        ad = item.find('span', attrs={'class': 'ad-badge-text'})
        if ad:
            print('광고 제외')
            print('='*80)
            continue
        # 
        name = name.split(', ')[0]
        # 가격
        price = item.find('strong', attrs={'class':'price-value'}).get_text()
        # 평점
        rate = item.find('em', attrs={'class':'rating'})
        if rate : 
            rate = rate.get_text()
            # print(rate)
        else:
            # rate = '평점 없음'
            continue

        # 리뷰수
        rate_count = item.find('span', attrs={'class': 'rating-total-count'})
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
            # print(rate_count)
        else: 
            rate_count='리뷰수 없음'

        if float(rate) <= 4.5 or float(rate_count) <= 100:
            # print('인기 제품 아님')
            # print('='*80)
            continue

        print('제품명 :', name)
        print('가격 :', price)
        print('평점 :', rate)
        print('리뷰수 :', rate_count)
        print('='*80)
