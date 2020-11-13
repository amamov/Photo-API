import requests
from flask import jsonify, request
from api_v1 import api
from scrapers.NaverPhoto import NaverPhoto
from scrapers.GooglePhoto import GooglePhoto
from scrapers.InstaPhoto import InstaPhoto


@api.route("/photos")
def photos():
    return (
        jsonify(
            [
                {"naver": "/api/v1/photos/naver/<keyword>"},
                {"google": "/api/v1/photos/google/<keyword>"},
                {
                    "instagram": "/api/v1/photos/instagram/<keyword> or\
                         /api/v1/photos/insta/<keyword>"
                },
            ]
        ),
        200,
    )


# 스레드 분리해서 각 site마다 병렬로 사진 가져오기
@api.route("/photos/<site>/<keyword>")
def photos_search(site, keyword):
    if site == "naver":
        photo = NaverPhoto(keyword)
        photo.scrape()
        return jsonify(photo.images), 200
    elif site == "google":
        photo = GooglePhoto(keyword)
        photo.scrape()
        return jsonify(photo.images), 200
    elif site == "instagram" or site == "insta":
        photo = InstaPhoto(keyword)
        photo.scrape()
        return jsonify(photo.images), 200
    else:
        return jsonify(), 400
