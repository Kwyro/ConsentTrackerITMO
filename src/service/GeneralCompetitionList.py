from typing_extensions import Optional

from ITMO.CompetitionListParser import getStudentList
from ITMO.dto.Student import Student
from ITMO.dto.Status import Status

from consent.DataParser import parse
from consent.ConsentParser import processing, getConsent

from service.dto.ConsentStudent import ConsentStudent

def getGeneralConsentList(programCode: str) -> list[ConsentStudent]:
    """Получение списка студентов на направлении с информацией о согласиях

    Args:
        programCode (str): Код программы
    
    Returns:
        list[ConsentStudent]: массив с информацией о каждом студенте, какой у него статус рекомендованного и куда было подано согласие
    """

    studentList: list[Student] = getStudentList(programCode)

    students: list[ConsentStudent] = list()

    for student in studentList:
        studentId: int = student.id
        studentStatus: Status = student.status
        consent: Optional[str] = getConsent(processing(parse(studentId)))

        students.append(ConsentStudent(studentId, studentStatus, consent))

    return students