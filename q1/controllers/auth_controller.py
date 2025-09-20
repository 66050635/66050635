from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repository.json_store import get_student_by_email

auth_bp = Blueprint("auth", __name__)

@auth_bp.get("/login")
def login():
    return render_template("login.html")

@auth_bp.post("/login")
def do_login():
    email = request.form.get("email","").strip()
    password = request.form.get("password","").strip()
    user = get_student_by_email(email)
    if not user or user["password"] != password:
        flash("อีเมลหรือรหัสผ่านไม่ถูกต้อง")
        return redirect(url_for("auth.login"))
    session["email"] = user["email"]
    session["student_id"] = user["student_id"]
    session["role"] = user["role"]
    if user["role"] == "admin":
        return redirect(url_for("admin.students"))
    else:
        return redirect(url_for("student.profile"))

@auth_bp.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
