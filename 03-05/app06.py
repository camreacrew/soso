# 숫자 2개를 입력받아 덧셈을 해서 출력
# 함수 2개

from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/test")
def stert():
    return render_template("sta.html")

@app.route("/end")
def end():
    a = request.args.get('aaaa')
    b = request.args






app.run(debug=True)