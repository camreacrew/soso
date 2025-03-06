from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/add", methods=['get'])
def add_get():
    return render_template("add.html")

@app.route("/add", methods=['post'])
def add_post():
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num2'))
    num = num1 + num2
    return redirect(f"/result?num={num}")

@app.route("/result", methods=['get'])
def result():
    num = request.args.get("num")
    return render_template("plus.html", num=num)

app.run(debug=True)