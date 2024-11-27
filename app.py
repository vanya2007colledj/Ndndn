from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_id = request.args.get('user_id')
    username = request.args.get('username')
    # Здесь можно использовать информацию о пользователе
    return f"Добро пожаловать, {username}! Ваш ID: {user_id}"
