import json
from pathlib import Path
from typing import List, Optional

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "db.json"

def _load():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(db):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def get_student_by_email(email: str) -> Optional[dict]:
    db = _load()
    for s in db["students"]:
        if s["email"].lower() == email.lower():
            return s
    return None

def get_student_by_id(student_id: str) -> Optional[dict]:
    db = _load()
    for s in db["students"]:
        if s["student_id"] == student_id:
            return s
    return None

def list_students() -> List[dict]:
    return _load()["students"]

def get_subject(subject_id: str) -> Optional[dict]:
    db = _load()
    for sub in db["subjects"]:
        if sub["subject_id"] == subject_id:
            return sub
    return None

def list_subjects() -> List[dict]:
    return _load()["subjects"]

def list_structures() -> List[dict]:
    return _load()["subject_structures"]

def list_structures_by_curriculum(cur_id: str) -> List[dict]:
    return [s for s in list_structures() if s["curriculum_id"] == cur_id]

def list_registered_for_student(student_id: str) -> List[dict]:
    return [r for r in _load()["registered"] if r["student_id"] == student_id]

def get_registration(student_id: str, subject_id: str) -> Optional[dict]:
    for r in _load()["registered"]:
        if r["student_id"] == student_id and r["subject_id"] == subject_id:
            return r
    return None

def add_registration(student_id: str, subject_id: str):
    db = _load()
    db["registered"].append({"student_id": student_id, "subject_id": subject_id, "grade": None})
    _save(db)

def update_grade(student_id: str, subject_id: str, grade: str):
    db = _load()
    for r in db["registered"]:
        if r["student_id"] == student_id and r["subject_id"] == subject_id:
            r["grade"] = grade
            break
    _save(db)
