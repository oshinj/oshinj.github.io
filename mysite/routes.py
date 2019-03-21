from flask import Flask, render_template
from mysite import app

@app.route("/")
def home() :
    return render_template('home.html')

@app.route("/projects/")
def projects() :
    return render_template('projects.html')

@app.route("/about/")
def about() :
    return render_template('about.html')

# @app.route("/hello<string:name>/")
# def hello(name) :
#     return render_template('hello.html', name=name)
