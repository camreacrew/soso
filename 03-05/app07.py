from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/start")
def start():
    return render_template("start02.html")

@app.route("/end")
def end():
    value1 = int(request.args.get("value1"))
    value2 = int(request.args.get("value2"))
    result = value1 + value2
    return render_template("end02.html", result=result)

app.run(debug=True)