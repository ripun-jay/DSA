from flask import Flask

app = Flask(__name__)

@app.route("/")
def fz():
    #l = input("ln")
    name = "ripunjay"
    return name

app.run(debug=True)
