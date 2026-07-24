from ITMO.dto.Status import Status

class Student:
    def __init__(self, id: int, recommendation: str | None, consent: bool):
        self.id = id
        self.status: Status = self.getStatus(recommendation, consent)

    @classmethod
    def getStatus(cls, recommendation: str, consent: bool) -> Status:
        if recommendation == "recommended" and consent:
            return Status.GREEN
        elif recommendation == "recommended" and (not consent):
            return Status.YELLOW
        elif recommendation == "pass_another":
            return Status.GRAY
        return Status.WHITE