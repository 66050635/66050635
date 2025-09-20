import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "db.json"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def main():
    students = []
    students.append({"student_id":"69009999","title":"นาย","first_name":"ผู้ดูแล","last_name":"ระบบ","birthdate":"1995-06-15","school":"KMITL","email":"admin@demo.ac.th","curriculum_id":"10000001","role":"admin","password":"admin123"})
    thai_students = [
        ("69000001","นาย","ภูริ","ศรีวงศ์","2007-03-21","เตรียมอุดมศึกษา","69000001@kmitl.ac.th","10000001"),
        ("69000002","นางสาว","ปพิชญา","วิริยะกุล","2008-10-04","สวนกุหลาบวิทยาลัย","69000002@kmitl.ac.th","10000001"),
        ("69000003","นาย","ธนกฤต","เจริญสุข","2007-12-12","บดินทรเดชา","69000003@kmitl.ac.th","10000001"),
        ("69000004","นางสาว","ชุติมา","พงษ์ศักดิ์","2008-05-11","สาธิต มศว.","69000004@kmitl.ac.th","10000001"),
        ("69000005","นาย","ปณต","วงศ์วรรณ","2007-08-30","สตรีวิทยา","69000005@kmitl.ac.th","10000001"),
        ("69000006","นางสาว","กัญญารัตน์","จรูญจิต","2008-01-19","บางกอกคริสเตียน","69000006@kmitl.ac.th","20000001"),
        ("69000007","นาย","ชยพล","แสงทวี","2007-04-07","อัสสัมชัญ","69000007@kmitl.ac.th","20000001"),
        ("69000008","นางสาว","ธิดารัตน์","ศิริธรรม","2008-09-09","สาธิตเกษตร","69000008@kmitl.ac.th","20000001"),
        ("69000009","นาย","ปรเมศวร์","อินทรา","2007-11-22","เตรียมอุดมศึกษาพัฒนาการ","69000009@kmitl.ac.th","20000001"),
        ("69000010","นางสาว","ณัฐมน","จิตรากุล","2008-02-02","สาธิตจุฬาฯ","69000010@kmitl.ac.th","20000001")
    ]
    for sid, title, fn, ln, bd, school, email, cur in thai_students:
        students.append({"student_id":sid,"title":title,"first_name":fn,"last_name":ln,"birthdate":bd,"school":school,"email":email,"curriculum_id":cur,"role":"student","password":"s1234567"})
    subjects = [
        {"subject_id":"05500001","name":"คอมพิวเตอร์เบื้องต้น","credits":3,"lecturer":"รศ.ดร. สุนทร","prerequisite_id":None},
        {"subject_id":"05500002","name":"การเขียนโปรแกรม 1","credits":3,"lecturer":"ผศ.ดร. ชาญชัย","prerequisite_id":None},
        {"subject_id":"05500003","name":"การเขียนโปรแกรม 2","credits":3,"lecturer":"ผศ.ดร. ชาญชัย","prerequisite_id":"05500002"},
        {"subject_id":"05500004","name":"คณิตศาสตร์สำหรับคอมพิวเตอร์","credits":3,"lecturer":"ผศ.ดร. อรทัย","prerequisite_id":None},
        {"subject_id":"90690001","name":"ภาษาไทยเพื่อการสื่อสาร","credits":2,"lecturer":"อาจารย์ กชกร","prerequisite_id":None},
        {"subject_id":"90690002","name":"ภาษาอังกฤษพื้นฐาน","credits":2,"lecturer":"อาจารย์ ไอลดา","prerequisite_id":None},
        {"subject_id":"05500005","name":"พีชคณิตเชิงเส้น","credits":3,"lecturer":"ผศ.ดร. วิทวัส","prerequisite_id":None},
        {"subject_id":"05500006","name":"โครงสร้างข้อมูล","credits":3,"lecturer":"ผศ.ดร. วิทวัส","prerequisite_id":"05500002"},
        {"subject_id":"05500007","name":"สถาปัตยกรรมคอมพิวเตอร์","credits":3,"lecturer":"อาจารย์ รัชกฤช","prerequisite_id":None},
        {"subject_id":"05500008","name":"แคลคูลัส 1","credits":3,"lecturer":"อาจารย์ ณัฐพงศ์","prerequisite_id":None},
        {"subject_id":"05500009","name":"แคลคูลัส 2","credits":3,"lecturer":"อาจารย์ ณัฐพงศ์","prerequisite_id":"05500008"}
    ]
    structures = []
    cur1 = "10000001"
    cur2 = "20000001"
    for sid in ["05500001","05500002","05500004","05500008"]:
        structures.append({"curriculum_id":cur1,"curriculum_name":"วิทยาการคอมพิวเตอร์","department_name":"คณะวิทยาศาสตร์","subject_id":sid,"term":1})
    for sid in ["05500003","05500005","05500006","05500007"]:
        structures.append({"curriculum_id":cur1,"curriculum_name":"วิทยาการคอมพิวเตอร์","department_name":"คณะวิทยาศาสตร์","subject_id":sid,"term":2})
    for sid in ["05500001","90690001","05500008"]:
        structures.append({"curriculum_id":cur2,"curriculum_name":"การจัดการเทคโนโลยีดิจิทัล","department_name":"คณะเทคโนโลยีสารสนเทศ","subject_id":sid,"term":1})
    for sid in ["90690002","05500005","05500007"]:
        structures.append({"curriculum_id":cur2,"curriculum_name":"การจัดการเทคโนโลยีดิจิทัล","department_name":"คณะเทคโนโลยีสารสนเทศ","subject_id":sid,"term":2})
    registered = []
    registered.extend([
        {"student_id":"69000001","subject_id":"05500002","grade":"B+"},
        {"student_id":"69000001","subject_id":"05500008","grade":"A"},
        {"student_id":"69000002","subject_id":"05500002","grade":"B"},
        {"student_id":"69000003","subject_id":"05500008","grade":"C+"},
        {"student_id":"69000004","subject_id":"05500002","grade":"A"},
        {"student_id":"69000006","subject_id":"90690001","grade":"A"},
        {"student_id":"69000006","subject_id":"05500008","grade":"B+"}
    ])
    db = {"students": students, "subjects": subjects, "subject_structures": structures, "registered": registered}
    DB_PATH.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Seeded {DB_PATH}")

if __name__ == "__main__":
    main()
