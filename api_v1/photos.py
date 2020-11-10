import requests
from flask import jsonify, request
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


# post 방식으로 데이터를 가져오자! (띄어쓰기 문제)
# 네이버는 성인인증이 필요한 경우면 크롤링 불가능

# @api.route("/photos/<site>", methods=['POST', 'GET'])
# def photos_search(site):
#     if request.method='POST':
#         if site == "naver" or site == "NAVER":
#             keyword=request.get_json()
#             photo = NaverPhoto(keyword)
#             photo.scrape()
#             return jsonify(photo.images), 200
#         else:
#             return jsonify(), 400