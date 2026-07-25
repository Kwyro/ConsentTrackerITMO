import requests
from requests import Response

def parse(token: str, studentID: int) -> list[dict]:
    """Парсит данные студента по ID его заявления.

    Args:
        studentID (int): ID заявления.

    Returns:
        list[dict]: Массив направлений.
    """

    URL: str = "https://vuzstat.ru/api/applicant-overview"

    headers: dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": f"Bearer {token}",
        "Referer": "https://vuzstat.ru/applicants/1214121",
    } 

    params: dict[str, int] = {
        "user_id": studentID
    }

    response: Response = requests.get(url=URL, headers=headers, params=params)

    return response.json()["applications"]

def getToken(email: str, password: str) -> str:
    """Получает JWT-токен, чтобы подавать API-запросы

    Args:
        email (str): Почта, на которую зарегестрирован аккаунт в ВУЗСтат
        password (str): Пароль от аккаунта

    Returns:
        str: JWT-токен
    """

    url = "https://vuzstat.ru/api/auth/login"

    headers: dict[str, str] = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://vuzstat.ru",
        "Referer": "https://vuzstat.ru/login",
    }

    payload: dict[str, str] = {
        "email": email,
        "password": password,
    }

    response: Response = requests.post(
        url,
        headers=headers,
        json=payload,  
    )

    return response.json()["token"]