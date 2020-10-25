from flask import render_template, request
from roniya.models import Users
from roniya import app


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['POST'])
def login():

    username = request.form['user']
    password = request.form['pass']

    result = Users.query.filter_by(username=username).first()
    if(result != None):
        return "success"
    else:
        return "failed"
