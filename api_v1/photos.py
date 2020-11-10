import requests
from flask import jsonify
from api_v1 import api
from scraper import NaverPhoto


@api.route("/photos")
def photos():
    return jsonify(), 200


@api.route("/photos/<site>/<keyword>")
def photos_search(site, keyword):
    if site == "naver" or site == "NAVER":
        photo = NaverPhoto(keyword)
        photo.scrape()
        return jsonify(photo.images), 200
    else:
        return jsonify(), 400
