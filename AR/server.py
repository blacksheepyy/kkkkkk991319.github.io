from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "TEST"

@app.route("/ar")
def render_static():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5005)