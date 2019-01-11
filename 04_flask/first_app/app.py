from flask import Flask

app = Flask(__name__)

@app.route('/ssafy') # decorator 꾸며주는애
def index():
    return 'Hi'

if __name__ == '__main__':
    app.run(debug=True) # 서버 일해..
