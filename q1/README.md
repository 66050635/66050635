python3 -m venv .venv
.\.venv\Scripts\Activate.ps1

# ติดตั้ง dependencies
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# ถ้าต้องการรีเซ็ตฐานข้อมูลตัวอย่าง
python repository/seed_data.py

# รันแอป
python app.py