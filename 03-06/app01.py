from flask import Flask, render_template, request, redirect

# 객체 : 데이터 + 함수
# 클래스 : 객체를 만드는 설계도, 대문자로 시작하는데 파이썬 클래스들을 소문자
# 클래스를 가지고 개체를 만드는 함수가 클래스 이름과 같다 : 생성자 (constructor)

app=Flask(__name__)

nums = []

# /nums라는 url은 배열에 데이터를 추가하는 작업을 담당
# 보통 웹 작업은 화면 보여주기(get)처리로 구성
@app.route("/nums", methods=['get'])
def input():
    return render_template("input.html")

@app.route("/nums", methods=['post'])
def process():
    value = request.form.get('value')
    nums.append(value)
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html", nums=nums)

app.run(debug=True)