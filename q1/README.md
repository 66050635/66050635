python3 -m venv .venv
source .venv/bin/activate

# ติดตั้ง dependencies
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# ถ้าต้องการรีเซ็ตฐานข้อมูลตัวอย่าง
python3 repository/seed_data.py

# รันแอป
python3 app.py