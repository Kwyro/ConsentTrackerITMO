from typing_extensions import Optional
from ITMO.dto.Status import Status

class ConsentStudent:
    def __init__(self, id: int, status: Status, consent: Optional[str]) -> None:
        self.id = id           # ID студента
        self.status = status   # Рекомендация
        self.consent = consent # Куда было подано согласие