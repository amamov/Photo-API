import requests
from flask import jsonify, request
from api_v1 import api
from scrapers import NaverPhoto, GooglePhoto


@api.route("/photos")
def photos():
    return (
        jsonify(
            [
                {"naver": "/api/v1/photos/naver/<keyword>"},
                {"google": "/api/v1/photos/google/<keyword>"},
            ]
        ),
        200,
    )


# 스레드 분리해서 각 site마다 병렬로 사진 가져오기
@api.route("/photos/<site>/<keyword>")
def photos_search(site, keyword):
    if site == "naver" or site == "NAVER" or site == "Naver":
        photo = NaverPhoto(keyword)
        photo.scrape()
        return jsonify(photo.images), 200
    elif site == "google" or site == "GOOGLE" or site == "Google":
        photo = GooglePhoto(keyword)
        photo.scrape()
        return jsonify(photo.images), 200
    else:
        return jsonify(), 400
