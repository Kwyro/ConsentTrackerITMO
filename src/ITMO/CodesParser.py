import requests

def getCodes() -> dict[str, int]:
    """По коду программы получает ID, который требуется для выполнения API-запросов

    Returns:
        dict[str, int]: Хэш-таблица, где храняться все коды программ с их ID
    """
    URL = "https://abitlk.itmo.ru/api/v1/rating/directions?degree=bachelor"

    responce = requests.get(url=URL).json()

    # Получим список всех программ по коду
    result = responce["result"] 
    items = result["items"]    

    programs: dict[str, int] = dict()

    for item in items:
        code = item['direction_title'][0:8]
        id = item['competitive_group_id']

        programs[code] = id

    return programs