import requests
from requests import Response
# pyrefly: ignore [missing-import]
from bs4 import BeautifulSoup
import json

from ITMO.dto.Student import Student
from ITMO.CodesParser import getCode

def getStudentList(programCode: str) -> list[Student]:
    """Получение списка студентов ИТМО

    Args:
        programCode (str): код программы

    Returns:
        list[Student]: массив с ID заявлений студентов и их рекомендацией 
    """

    programId: int = getCode(programCode)
    URL: str = f"https://abit.itmo.ru/_next/data/{getBuildId()}/ru/ranking/bachelor/budget/{programId}.json?degree=bachelor&financing=budget&id={programId}" 

    response: Response = requests.get(url=URL)

    # Получение сырого списка студентов
    pageProps = response.json()["pageProps"]
    programList = pageProps["programList"]

    generalCompetition = programList["general_competition"]

    students: list[Student] = list()

    for student in generalCompetition:
        id = student["sspvo_id"]
        recommendation = student["status"]
        isSendConsent = student["is_send_agreement"]

        students.append(Student(id, recommendation, isSendConsent))

    return students

def getBuildId() -> str:
    """Возвращает BuildId, который нужен, чтобы делать API-запросы для получения списков

    Returns:
        str: BuildId NextJS
    """
    URL: str = "https://abit.itmo.ru/rankings/bachelor"
    
    response: Response = requests.get(URL)
    html: str = response.text

    soup: BeautifulSoup = BeautifulSoup(html, "html.parser")

    data: dict = json.loads(soup.find("script", id="__NEXT_DATA__").string)
    build_id: str = data["buildId"]

    return build_id
