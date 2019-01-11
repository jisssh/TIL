import random
from flask import Flask, jsonify # 리스트를 세상 밖으로 보여주는 애

app = Flask(__name__)

my_dictionary = {
    'apple':'사과',
    'banana':'바나나',
    'orange':'오렌지',
    'lunch':'점심',
    'chicken':'치킨'
}

@app.route('/') # decorator 꾸며주는애
def index():
    return 'Hi, I am JISS'

@app.route('/ssafy')
def ssafy():
    return 'ssssssssafy'

@app.route('/hi/<string:name>')
def hi(name):
    return(f'hi {name}!')

@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1, 46),6)
    return jsonify(numbers)

@app.route('/dictionary/<string:word>')
def dictionary(word):
        if word in my_dictionary:
            return (f'{word}은(는) {my_dictionary[word]}!')
        else:
            return (f'{word}은(는) 나만의 단어장에 없는 단어입니다!')
if __name__ == '__main__':
    app.run(debug=True) # 서버 일해..
