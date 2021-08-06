from flask_ngrok import run_with_ngrok
from flask import Flask, render_template
app = Flask(__name__)

run_with_ngrok(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_details")
def get_d():
    return "something2"

@app.route("/test")
def test():
    return "something3"

if __name__ == "__main__":
    app.run()
