from urllib.parse import quote_plus
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests


class GooglePhoto:

    """
    [GooglePhoto Class]
    Author : Yoon - Snag Seok
    Date : 20.11.11
    구글 사진 스크래핑 (50장)
    """

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
    pass
