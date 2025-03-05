# 플라스크 모듈로 부터 Flask 클래스를 읽어온다
from flask import Flask

# Flask를 이용해서 플라스크 앱을 생성
app = Flask(__name__)

# 사용자가 웹브라우저로 요청하면 실행되는 함수
# decorator로 주소를 지정 : 웹 서버 주소 + 데코레이터 주소
# 127.0.0.1:5000/test1
@app.route("/test1")
def rest1():
    return " Hello Flask"


# 플라스크앱(파이썬 서버) 실행
# debug옵션은 코드가 변경되면 서버 재시작
app.run(debug=True)