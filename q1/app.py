from flask import Flask, session, redirect, url_for, render_template
from controllers.auth_controller import auth_bp
from controllers.student_controller import student_bp
from controllers.admin_controller import admin_bp
from controllers.registration_controller import reg_bp
from repository.json_store import list_students
import threading, webbrowser, time, os, sys

app = Flask(__name__)
app.secret_key = "dev-secret-key"

app.register_blueprint(auth_bp)
app.register_blueprint(student_bp, url_prefix="/student")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(reg_bp, url_prefix="/register")

@app.route("/")
def index():
    role = session.get("role")
    if role == "admin":
        return redirect(url_for("admin.students"))
    elif role == "student":
        return redirect(url_for("student.profile"))
    return redirect(url_for("auth.login"))

@app.route("/accounts")
def accounts():
    users = list_students()
    users_sorted = sorted(users, key=lambda u: (u["role"]!="admin", u["student_id"]))
    return render_template("accounts.html", users=users_sorted)

def _open_browser(url):
    try:
        if os.environ.get("WSL_DISTRO_NAME"):
            try:
                b = webbrowser.get("windows-default")
                b.open(url)
                return
            except:
                pass
        webbrowser.open(url)
    except Exception:
        pass

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"
    threading.Thread(target=lambda: (time.sleep(1.0), _open_browser(url)), daemon=True).start()
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
