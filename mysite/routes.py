from flask import Flask, render_template
from mysite import app

@app.route("/")
def index() :
    return render_template('home.html')

@app.route("/hello<string:name>/")
def hello(name) :
    return render_template('hello.html', name=name)
