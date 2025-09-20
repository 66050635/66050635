from flask import Blueprint, render_template, session, redirect, url_for
from repository.json_store import get_student_by_id, list_registered_for_student, get_subject
from models.rules import age_at_least_15

student_bp = Blueprint("student", __name__)

def login_required_student():
    if session.get("role") != "student":
        return False
    return True

@student_bp.get("/profile")
def profile():
    if not login_required_student():
        return redirect(url_for("auth.login"))
    sid = session["student_id"]
    student = get_student_by_id(sid)
    regs = list_registered_for_student(sid)
    rows = []
    for r in regs:
        sub = get_subject(r["subject_id"])
        rows.append({"subject_id": sub["subject_id"],"name": sub["name"],"credits": sub["credits"],"grade": r["grade"] or "-"})
    age_ok = age_at_least_15(student["birthdate"])
    return render_template("student_profile.html", student=student, rows=rows, age_ok=age_ok)
