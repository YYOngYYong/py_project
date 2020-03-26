import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309'
data = requests.get(url,headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
selecters = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# title  = soup.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis')

# select를 이용해서, tr들을 불러오기
rank = 1
for selecter in selecters:
    title_tag = selecter.select_one('td.info > a.title.ellipsis')
    artists = selecter.select_one('td.info > a.artist.ellipsis')
    if title_tag is not None:
        # a의 text를 찍어본다.
        print(rank,title_tag.text.strip(),':',artists.text)
        rank+=1
#############################