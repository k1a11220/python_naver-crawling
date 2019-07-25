import requests
from bs4 import BeautifulSoup
import pandas

# 웹 크롤링 작업을 실행해주는 함수
def crawling(code, page_count):
    # url 조합
    front_url = "http://search.daum.net/search?w=news&nil_search=btn&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q="
    back_url = "&p="

    # 결과를 저장해줄 result 배열 선언
    result = []
    # page_count까지 페이지를 넘겨가면서 탐색할 수 있도록 for문으로 반복
    for i in range(1, page_count + 1):
        url = front_url + code + back_url + str(i)
        # 실제로 구성된 url이 어떻게 나오는지 확인할 수 있도록 print
        print(url)


        # requests 라이브러리의 get함수에 url을 인자값으로 하여 실행해주면 페이지 결과를 쉽게 가져올 수 있습니다.
        temp_result = requests.get(url)
        # 페이지 결과에서 우리가 원하는 결과만 손쉽게 가져올 수 있도록 BeautifulSoup을 이용하여 xml형태로 구조화해줍니다.
        print(temp_result.text)
        soup = BeautifulSoup(temp_result.text, "lxml")
        # 구조화된 결과에서 우리가 원하는 a태그, 그리고 그중에서 class가 f_link_b인 결과만 select로 가져옵니다.
        titles = soup.select('a.f_link_b')

        for j in range(len(titles)):
            # 결과가 잘 나오고 있는지 print 해봅니다.
            print(titles[j].text.strip())
            # 결과를 result 배열에 추가해줍니다.
            result.append(titles[j].text.strip())

    return result

    def main():
    # code 값과 page_count를 정해줍니다.
    code = "비트코인"
    page_count = 2

    # 위 두 변수를 인자로 하여 crawling를 실행합니다.
    result = crawling(code, page_count)
    # 결과를 출력합니다.
    print(result)

# main함수를 실행해줍니다.
main()
