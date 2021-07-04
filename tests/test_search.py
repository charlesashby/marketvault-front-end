import unittest

from app.utils.search import MySQLClient, Interval


class TestSearchUtils(unittest.TestCase):

    def test_mysql_client(self):
        client = MySQLClient()
        result = client.search_stores(
            category="art",
            daily_visitors=Interval(0, 10000),
            alexa_rank=Interval(0, 1000000),
            topic=None
        )
        assert len(result) > 0

        topics = client.search_topic_by_substring("fidget")

        related_stores = client.search_stores(
            category=None,
            daily_visitors=None,
            alexa_rank=None,
            topic=topics[0].id
        )

        assert any("fidget" in s.description for s in related_stores)
        assert client.random_topic(1) != client.random_topic(1)

    def test_iterator(self):
        ...