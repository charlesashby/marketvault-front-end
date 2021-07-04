from flask import render_template, Blueprint, request

from app.utils.search import MySQLClient
from app.utils.preprocessor import TextPreprocessor


mainbp = Blueprint("main", __name__)


@mainbp.route("/search", methods=["GET"])
@mainbp.route("/", methods=["GET"])
def home():
    stores_by_page = 10
    topic = request.args.get("topic")
    category = request.args.get("category")
    daily_visitors = request.args.get("dailyvisitors")
    alexa_rank = request.args.get("alexarank")
    page = request.args.get("page") or 0

    if all([topic is None, category is None, daily_visitors is None, alexa_rank is None]):
        stores = MySQLClient.random_stores(page * stores_by_page, stores_by_page)
    else:
        stores = MySQLClient.search_stores(category, daily_visitors, alexa_rank, topic, page * stores_by_page, stores_by_page)

    stores = [
        {
            "url": store.url,
            "description": TextPreprocessor.clean_str(store.description),
            "title": TextPreprocessor.clean_str(store.title),
            "alexa_rank": store.alexa_rank,
            "category": store.category,
            "average_product_price": store.average_product_price,
            "daily_visitors": store.daily_visitors
        } for store in stores
    ]

    return render_template("search/index.html", stores=stores)


@mainbp.route("/search/topics", methods=["GET"])
def search_topics():
    substring = request.args.get("q")
    return [
        {
            "id": topic.id,
            "text": topic.text
        } for topic in MySQLClient.search_topic_by_substring(substring)
    ]


