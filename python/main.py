from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://api.saramin.co.kr/job-search?keywords=%EC%9B%B9+%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%85%94"
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close() # urlopen을 진행한 후에는 close를 한다.

soup = BeautifulSoup(source, "html5lib") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름
table = soup.find(id="Top-Box-Office")
movies = table.find_all(class_="middle_col")

for movie in movies:
    title = movie.get_text()
    print(title, end=' ')
    link = movie.a.get('href')
    url = 'http://api.saramin.co.kr/job-search?keywords=%EC%9B%B9+%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%85%94' + link
    print(url)