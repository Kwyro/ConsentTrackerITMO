def processing(programs: list[dict]) -> dict[str, bool]:
    """Обрабатывает сырые данные

    Args:
        programs (list[dict]): список сырых JSON со всеми программами

    Returns:
        dict[str, bool]: хэш-таблица с названиями ВУЗов и имением согласия
    """
    
    universities: dict[str, bool] = dict()

    for program in programs:
        name: str = program["short_name"]
        consent: bool = True if program["consent"] == "ONLINE" else False
        
        universities[name] = consent

    return universities
            