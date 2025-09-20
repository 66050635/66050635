from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repository.json_store import list_structures_by_curriculum, list_registered_for_student, get_subject, add_registration
from models.rules import can_register

reg_bp = Blueprint("reg", __name__)

def login_required_student():
    return session.get("role") == "student"

@reg_bp.get("/courses")
def courses():
    if not login_required_student():
        return redirect(url_for("auth.login"))
    sid = session["student_id"]
    from repository.json_store import get_student_by_id
    st = get_student_by_id(sid)
    cur_id = st["curriculum_id"]
    structures = list_structures_by_curriculum(cur_id)
    reg = list_registered_for_student(sid)
    registered_sub_ids = set(r["subject_id"] for r in reg)
    def get_grade(prereq_id):
        for rr in reg:
            if rr["subject_id"] == prereq_id:
                return rr["grade"]
        return None
    rows = []
    for s in structures:
        if s["subject_id"] not in registered_sub_ids:
            sub = get_subject(s["subject_id"])
            rows.append({"subject_id": sub["subject_id"],"name": sub["name"],"term": s["term"],"credits": sub["credits"],"can_register": can_register(sub.get("prerequisite_id"), get_grade),"prereq": sub.get("prerequisite_id")})
    return render_template("course_list.html", rows=rows)

@reg_bp.post("/do_register")
def do_register():
    if not login_required_student():
        return redirect(url_for("auth.login"))
    sid = session["student_id"]
    subject_id = request.form.get("subject_id")
    reg = list_registered_for_student(sid)
    def get_grade(prereq_id):
        for rr in reg:
            if rr["subject_id"] == prereq_id:
                return rr["grade"]
        return None
    sub = get_subject(subject_id)
    if not sub:
        flash("ไม่พบรายวิชา")
        return redirect(url_for("reg.courses"))
    if not can_register(sub.get("prerequisite_id"), get_grade):
        flash("ยังไม่ผ่านวิชาบังคับก่อน ไม่สามารถลงทะเบียนวิชานี้ได้")
        return redirect(url_for("reg.courses"))
    add_registration(sid, subject_id)
    flash("ลงทะเบียนสำเร็จ")
    return redirect(url_for("student.profile"))
