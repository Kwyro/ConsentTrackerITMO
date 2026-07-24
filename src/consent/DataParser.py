import requests
from requests import Response

def parse(studentID: int) -> list[dict]:
    """ Парсит данные студента по ID его заявления

    Args:
        studentID (int): ID заявления
        
    Returns:
        list[dict]: массив, в котором указаны все ВУЗы с направленями
    """

    URL: str = "https://www.postupashkin.ru/priem-2026/forecast?app=" + str(studentID)

    response: Response = requests.get(url=URL)
    positions = response.json()["positions"]

    return positions