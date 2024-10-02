from flask import Flask, redirect, url_for, request, render_template_string, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask import session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Thay thế bằng secret key của bạn
login_manager = LoginManager()
login_manager.init_app(app)

# Tạo một lớp User
class User(UserMixin):
    def __init__(self, username):
        self.id = username  # Thiết lập thuộc tính id cho người dùng
        self.username = username    

# Tạo một đối tượng người dùng mẫu cho việc xác thực
users = {'admin': 'asdfghjkl@@ASDFGHJKL'}  # Tên người dùng và mật khẩu
url_dashboard = "http://127.0.0.1:8081"
@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None


@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')


# Trang login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Xóa session trước khi đăng nhập
        session.clear()
        
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            user = User(username)
            login_user(user)
            return redirect(f"{url_dashboard}/dashboard")  # Chuyển hướng đến dashboard
        else:
            return redirect(f"{url_dashboard}/unauthorized")
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=8080)
