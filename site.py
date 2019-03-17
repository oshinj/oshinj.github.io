from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index() :
    return render_template('home.html')

@app.route("/hello/<string:name>/")
def hello(name) :
    return render_template('hello.html', name=name)

@app.route("/members")
def members() :
    return "Members"

if __name__ == "__main__" :
    app.run(debug=True, host='0.0.0.0', port=80)
