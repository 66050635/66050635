from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from repository.json_store import list_students, get_student_by_id, list_registered_for_student, list_subjects, update_grade
from models.rules import grade_is_valid

admin_bp = Blueprint("admin", __name__)

def admin_required():
    return session.get("role") == "admin"

@admin_bp.get("/students")
def students():
    if not admin_required():
        return redirect(url_for("auth.login"))
    q = request.args.get("q","").lower().strip()
    school = request.args.get("school","").lower().strip()
    sort = request.args.get("sort","")
    all_std = list_students()
    def full_name(s): return (s["first_name"] + " " + s["last_name"]).lower()
    rows = []
    for s in all_std:
        if s["role"] == "admin":
            continue
        if q and (q not in full_name(s)) and (q not in s["student_id"]):
            continue
        if school and school not in s["school"].lower():
            continue
        rows.append(s)
    if sort == "name":
        rows.sort(key=lambda x: (x["first_name"], x["last_name"]))
    elif sort == "age":
        from dateutil import parser
        from datetime import date
        def age(x):
            bd = parser.isoparse(x["birthdate"]).date()
            today = date.today()
            return today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
        rows.sort(key=lambda x: age(x), reverse=True)
    return render_template("admin_students.html", rows=rows, q=q, school=school, sort=sort)

@admin_bp.get("/student/<student_id>")
def student_detail(student_id):
    if not admin_required():
        return redirect(url_for("auth.login"))
    s = get_student_by_id(student_id)
    regs = list_registered_for_student(student_id)
    from repository.json_store import get_subject
    details = []
    for r in regs:
        sub = get_subject(r["subject_id"])
        details.append({"subject_id": sub["subject_id"],"name": sub["name"],"credits": sub["credits"],"grade": r["grade"] or "-"})
    return render_template("student_profile.html", student=s, rows=details, admin_view=True)

@admin_bp.get("/grade-entry")
def grade_entry():
    if not admin_required():
        return redirect(url_for("auth.login"))
    subs = list_subjects()
    selected = request.args.get("subject_id")
    students_rows = []
    if selected:
        from repository.json_store import list_students, list_registered_for_student
        for s in list_students():
            if s["role"] == "admin":
                continue
            regs = list_registered_for_student(s["student_id"])
            for r in regs:
                if r["subject_id"] == selected:
                    students_rows.append({"student_id": s["student_id"],"name": f'{s["first_name"]} {s["last_name"]}',"grade": r["grade"] or ""})
    return render_template("admin_grade_entry.html", subjects=subs, selected=selected, students_rows=students_rows)

@admin_bp.post("/grade-entry")
def do_grade_entry():
    if not admin_required():
        return redirect(url_for("auth.login"))
    subject_id = request.form.get("subject_id")
    for key, val in request.form.items():
        if key.startswith("sid_"):
            sid = key.replace("sid_","")
            grade = val.strip()
            if grade:
                if not grade_is_valid(grade):
                    flash(f"เกรดของ {sid} ไม่ถูกต้อง")
                else:
                    update_grade(sid, subject_id, grade)
    flash("บันทึกเกรดสำเร็จ")
    return redirect(url_for("admin.grade_entry", subject_id=subject_id))
