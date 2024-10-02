from flask import Flask, redirect, render_template
from flask_login import LoginManager, UserMixin, login_required, current_user, logout_user
from flask import session

app = Flask(__name__) 
app.secret_key = 'your_secret_key'  # Thay thế bằng secret key của bạn
login_manager = LoginManager()
login_manager.init_app(app)

# Tạo một lớp User
class User(UserMixin):
    def __init__(self, username):
        self.username = username

# Tạo một đối tượng người dùng mẫu cho việc xác thực
users = {'admin': 'asdfghjkl@@ASDFGHJKL'}  # Tên người dùng và mật khẩu

@login_manager.user_loader
def load_user(username):
    return User(username) if username in users else None

@app.route('/dashboard')
@login_required
def dashboard():
    return f"Welcome to dashboard {current_user.username}"

@app.route('/unauthorized')
def unauthorized():
    return render_template('401.html'), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('http://127.0.0.1:8080')  # Chuyển hướng về trang login

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=8081)
