from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gift")
def gift():
    return render_template("message.html")

if __name__ == "__main__":
    app.run(debug=True)