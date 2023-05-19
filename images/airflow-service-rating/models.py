"""
Модуль с моделями
"""
from enum import Enum

from pydantic import BaseModel


class Score(int, Enum):
    """
    Модель, содержащая лайк или дизайк
    """

    LIKE = 1
    DISLIKE = -1


class GenerateResultInfo(BaseModel):
    """
    Модель с информации об одном результате генерации.
    post_id - int, айди поста в базе данных. На фронтенде наверное не понадобится
    user_id : int, айди юзера, который сделал пост, тоже не понадобится
    method : str, название метода, которым сделан этот текст
    hint : str, затравка/тема поста, введенные пользователем для генерации
    text : str, сам текст, который сделала нейросеть
    rating : int, оценка поста, целое число (Задать посту оценку - см. /send_feedback)
    date : int, unix дата, когда был отправлен запрос
    group_id : int, айди группы, для которой сделан пост
    status : str, [READY, NOT_READY, ERROR] - описание статуса запроса
    gen_time : int - количество миллисекунд, затраченных на генерацию. date + gen_time = дата, когда генерация закончена
    platform : str - платформа, с которой отправлен запрос
    published : int - 0 - не опубликовано, 1 - опубликовано
    """

    post_id: int
    user_id: int
    method: str
    hint: str
    text: str
    rating: int
    date: int
    group_id: int
    status: str
    gen_time: int
    platform: str
    published: int


class GenerateMethodCount(BaseModel):
    """
    Модель с результатом подсчёта вызовов определённых методов
    """

    method: str
    cnt: int
