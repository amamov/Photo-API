from urllib.parse import quote_plus
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests


class NaverPhoto:

    """ 네이버 사진 스크래핑 50장 (네이버는 성인인증이 필요한 경우면 크롤링 불가능) """

    BASE_URL = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="

    def __init__(self, keyword: str):
        self.keyword = quote_plus(keyword.strip())
        self.url = self.BASE_URL + self.keyword
        self.images = {
            "site": "naver",
            "keyword": keyword.strip(),
            "src": [],
        }

    def __str__(self):
        return self.keyword

    def scrape(self):
        with requests.Session() as session:
            headers = {
                "Referer": "https://www.naver.com/",
                "User-Agent": UserAgent().chrome,
            }
            response = session.get(self.url, headers=headers).text
            soup = BeautifulSoup(response, "html.parser")
            img_list = soup.select("div.img_area > a > img")
            if img_list:
                for img in img_list:
                    img_src = img["data-source"]
                    self.images["src"].append(img_src)


class GooglePhoto:

    """ 구글 사진 크롤링 """

    BASE_URL = "https://www.google.com/search?q="
    SEARCH_URL = "&sxsrf=ALeKk03MRCBotTPKt67gcfvlwd2mzg97Uw:1605097101396&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiK17vUvPrsAhWCBogKHVh2CEgQ_AUoAXoECAQQAw&cshid=1605097165583905&biw=724&bih=682"

    def __init__(self, keyword):
        self.keyword = quote_plus(keyword.strip())
        self.url = self.BASE_URL + self.keyword + self.SEARCH_URL
        self.images = {
            "site": "google",
            "keyword": keyword.strip(),
            "src": [],
        }

    def __str__(self):
        return self.keyword

    def scrape(self):
        with requests.Session() as session:
            headers = {
                "Referer": "https://www.google.com/",
                "User-Agent": UserAgent().chrome,
            }
            response = session.get(self.url, headers=headers).text
            soup = BeautifulSoup(response, "html.parser")
            img_list = soup.select("div.isv-r > a > div > img")
            if img_list:
                for img in img_list:
                    try:
                        img_src = img["data-src"]
                    except KeyError:
                        pass
                    else:
                        self.images["src"].append(img_src)


if __name__ == "__main__":
    photo1 = GooglePhoto("조이")
    photo1.scrape()
    print(photo1.images)
