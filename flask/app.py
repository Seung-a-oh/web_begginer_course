from flask import Flask, render_template, request, jsonify
app = Flask(__name__) #플라스크 애플리케이션을 생성하는 코드, name이라는 변수에는 모듈명이 담긴다.

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/') #특정 주소에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터
def home():
   return render_template('index.html')

#이게 API임
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give') #title_give로 가져온 값 여기다 찍어줘봐
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = '봄날은간다'
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)