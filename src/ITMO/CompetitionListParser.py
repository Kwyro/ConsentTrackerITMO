import requests
from requests import Response
# pyrefly: ignore [missing-import]
from bs4 import BeautifulSoup
import json

def getStudentList(programId: int) -> list:
    """Получает списко студентов, в котором 
    """

def getBuildId() -> str:
    """Получает BuildId, который нужен, чтобы делать API-запросы для получения списков

    Returns:
        str: BuildId NextJS
    """
    URL: str = "https://abit.itmo.ru/rankings/bachelor"
    
    response: Response = requests.get(URL)
    html: str = response.text

    soup = BeautifulSoup(html, "html.parser")

    data = json.loads(soup.find("script", id="__NEXT_DATA__").string)
    build_id = data["buildId"]

    return build_id
