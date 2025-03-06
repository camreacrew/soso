from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# 주소가 같아도 메소드의 값이 다르면 써도 상관 없음
@app.route("/login", methods=['get'])
def login_get():
    state = request.args.get('state', None)
    message = "로그인에 실패했습니다" if state!=None else ""
    return render_template("login.html")


@app.route("/login", methods=['post'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    if username=='spring' and password=='1234':
        return redirect("/success")
    else:
        return redirect("/login?state=fail")

@app.route("/success")
def success():
    return render_template("success.html")

app.run(debug=True)