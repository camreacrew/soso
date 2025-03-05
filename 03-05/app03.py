from flask import Flask,request

app = Flask(__name__)

# 127.0.0.1:5500 서버의 /주소로 요청을 보내면
# index 함수가 실행되서 html을 생성한 다음 사용자에게 보내준다
# html을 동적으로 생성한다 -> WAS
@app.route("/")
def index():
    return "<html><body><p>Hello <b>Flask</b></p></body></html>"

# 사용자가 127.0.0.1:5000/test2?username=spring으로 요청을 보내면
# spring이라는 username을 꺼내서 출력
@app.route("/test1")
def test1():
    # 클래스에는 값과 함수가 들어있다
    # 클레스타입의 변수를 객체라고 한다
    # 파이썬에서는 모든 것이 객체
    username = request.args.get('username')
    return username

# 127.0.0.1:5000/test1?value=11
def test2():
    value = request.args.get("value")
    return value+value

app.run(debug=True)