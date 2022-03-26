from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@app.route('/user-info', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    print(data)
    return render_template("user-info.html")

@app.route('/create-acc', methods=['GET', 'POST'])
def create_acc():
    data = request.form
    print(data)
    return render_template("create-acc.html")
