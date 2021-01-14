import os
from flask import Flask, render_template

app = Flask(__name__, template_folder=os.path.abspath("."))


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
