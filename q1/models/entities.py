from dataclasses import dataclass
from typing import Optional

@dataclass
class Student:
    student_id: str
    title: str
    first_name: str
    last_name: str
    birthdate: str
    school: str
    email: str
    curriculum_id: str
    role: str
    password: str

@dataclass
class Subject:
    subject_id: str
    name: str
    credits: int
    lecturer: str
    prerequisite_id: Optional[str] = None

@dataclass
class SubjectStructure:
    curriculum_id: str
    curriculum_name: str
    department_name: str
    subject_id: str
    term: int

@dataclass
class RegisteredSubject:
    student_id: str
    subject_id: str
    grade: Optional[str] = None
