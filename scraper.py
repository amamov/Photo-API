from urllib.parse import quote_plus
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests


class NaverPhoto:

    """ 네이버 사진 스크래핑 50장 """

    BASE_URL = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="

    def __init__(self, keyword: str):
        self.keyword = keyword.strip()
        self.url = self.BASE_URL + self.keyword
        self.images = {
            "site": "naver",
            "keyword": self.keyword,
            "src": [],
        }

    def __str__(self):
        return self.keyword

    def scrape(self):
        with requests.Session() as session:
            headers = {
                "User-Agent": UserAgent().chrome,
                "Referer": "https://www.naver.com/",
            }
            response = session.get(self.url, headers=headers).text
            soup = BeautifulSoup(response, "html.parser")
            img_list = soup.select("div.img_area > a > img")
            for img in img_list:
                img_src = img["src"]
                self.images["src"].append(img_src)


if __name__ == "__main__":
    photo1 = NaverPhoto("조이")
    photo1.scrape()
    print(photo1.images)