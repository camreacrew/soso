# 기능들의 집합 : 라이브러리(library)
# import없이 사용가능 : 내장

# 보통의 경우 라이브러리라고 하면 추가로 설치해서 사용한다.
# 라이브러리 : 단순한 기능의 집합
# 프레임워크 : 라이브러리 + 사용법

# 웹 프레임워크 : 사용자 요청 -> 처리 -> 사용자에게 응답

# 파이썬의 웹 프레임워크 : flask, django, fast api
# 자바의 웹프레임워크 : spring

# 클래스 이름은 대문자로 시작. 파이썬이 제공하는 클래스들은 소문자로 시작하는 경우도 있다
from flask import Flask

# 현재 모듈의 이름을 가지고 Flask앱을 생성
# python app01.py 이렇게 직접 실행한 경우 __name__은 "__main__"이 된다
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"

@app.route("/test1")
def test1():
    return "테스트 1번입니다"

@app.route("/test2")
def test2():
    return "테스트 2번입니다"

if __name__=='__main__':
    app.run(debug=True)