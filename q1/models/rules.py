from datetime import date
from dateutil import parser

VALID_GRADES = ["A","B+","B","C+","C","D+","D","F"]

def is_valid_student_id(sid: str) -> bool:
    return len(sid) == 8 and sid.isdigit() and sid.startswith("69")

def is_valid_subject_id(sub_id: str) -> bool:
    return len(sub_id) == 8 and sub_id.isdigit() and (sub_id.startswith("0550") or sub_id.startswith("9069"))

def is_valid_curriculum_id(cur_id: str) -> bool:
    return len(cur_id) == 8 and cur_id.isdigit() and not cur_id.startswith("0")

def age_at_least_15(birthdate_iso: str) -> bool:
    bd = parser.isoparse(birthdate_iso).date()
    today = date.today()
    age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
    return age >= 15

def can_register(prereq_id, get_grade_func) -> bool:
    if not prereq_id:
        return True
    g = get_grade_func(prereq_id)
    return g is not None

def grade_is_valid(grade: str) -> bool:
    return grade in VALID_GRADES
