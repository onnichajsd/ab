# app.py
from flask import Flask, render_template
from auth_routes import auth  # นำเข้า Blueprint สำหรับเส้นทางการเข้าสู่ระบบ

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # ใช้ในการเข้ารหัส session

# เชื่อมต่อ Blueprint สำหรับการเข้าสู่ระบบ
app.register_blueprint(auth)

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)

