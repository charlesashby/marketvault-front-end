from typing import Optional, List, Any

from dataclasses import dataclass
from sqlalchemy.sql.expression import func

from app import models


@dataclass
class Interval:
    left: float
    right: float

    def __post_init__(self):
        assert isinstance(self.left, (float, int))
        assert isinstance(self.right, (float, int))


class MySQLClient:

    @staticmethod
    def search_stores(
            category: Optional[str],
            daily_visitors: Optional[Interval],
            alexa_rank: Optional[Interval],
            topic: Optional[int],
            offset: int = 0,
            limit: int = 100
    ) -> List[models.Store]:

        query = models.Store.query

        if topic:
            query = query\
                .filter(models.Store.id == models.StoreTopic.store_id)\
                .filter(models.StoreTopic.topic_id == topic)

        if category:
            query = query.filter(models.Store.category == category)

        if daily_visitors:
            query = query.filter(
                models.Store.daily_visitors >= daily_visitors.left,
                models.Store.daily_visitors < daily_visitors.right
            )

        if alexa_rank:
            query = query.filter(
                models.Store.alexa_rank >= alexa_rank.left,
                models.Store.alexa_rank < alexa_rank.right
            )

        stores = query.limit(limit).offset(offset).all()
        return stores

    @staticmethod
    def search_topic_by_substring(substring: str, offset: int = 0, limit: int = 10) -> List[models.Topic]:
        topics = models.Topic.query.filter(models.Topic.text.like(f"%{substring}%")).offset(offset).limit(limit).all()
        return topics

    @staticmethod
    def search_store_title_by_substring():
        return NotImplementedError

    @staticmethod
    def search_store_description_by_substring():
        return NotImplementedError

    @staticmethod
    def random_topic(offset: int = 0, limit: int = 1) -> List[models.Topic]:
        return models.Topic.query.order_by(func.rand()).offset(offset).limit(limit).all()

    @staticmethod
    def random_stores(offset: int = 0, limit: int = 10) -> List[models.Store]:
        return models.Store.query.order_by(func.rand()).offset(offset).limit(limit).all()