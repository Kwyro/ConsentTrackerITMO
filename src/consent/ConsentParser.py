from typing_extensions import Optional

def processing(programs: list[dict]) -> dict[str, bool]:
    """Обрабатывает сырые данные и получает информацию о имение заявлений в ВУЗЫ

    Args:
        programs (list[dict]): список сырых JSON со всеми программами

    Returns:
        dict[str, bool]: хэш-таблица с названиями ВУЗов и имением согласия
    """
    
    universities: dict[str, bool] = dict()

    for program in programs:
        name: str = program["university"]
        consent: bool = True if program["consent"] == "ONLINE" else False
        
        universities[name] = consent

    return universities

def getConsent(universities: dict[str, bool]) -> Optional[str]:
    """Возвращает название ВУЗа, куда было согласие, в том случае, если было подано согласие

    Args:
        universities (dict[str, bool]): хэш-таблица с названиями ВУЗов и имением согласия
    
    Returns:
        Optional[str]: название ВУЗа, где лежит согласие
    """

    for name, consent in universities.items():
        if consent: return name
    return None