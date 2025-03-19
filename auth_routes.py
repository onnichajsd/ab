# auth_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session

auth = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    "admin": "1"  # ตัวอย่าง username และ password
}

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ตรวจสอบ username และ password
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['username'] = username  # เก็บข้อมูล username ใน session
            return redirect(url_for('auth.user'))  # ไปที่หน้า user เมื่อเข้าสู่ระบบสำเร็จ
        else:
            return "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง", 401  # ถ้าชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง

    return render_template('login.html')  # แสดงหน้า login ถ้าเป็น GET

@auth.route('/user')
def user():
    if 'username' in session:  # ตรวจสอบว่า session มี username หรือไม่
        username = session['username']  # ดึงข้อมูล username จาก session
        return render_template('user.html', username=username)  # ส่งชื่อผู้ใช้ไปที่ user.html
    return redirect(url_for('auth.login'))  # ถ้าไม่ได้เข้าสู่ระบบจะไปหน้า login

@auth.route('/logout')
def logout():
    session.pop('username', None)  # ลบข้อมูล session
    return redirect(url_for('index'))  # เปลี่ยนเส้นทางไปหน้า home หลังจากออกจากระบบ
