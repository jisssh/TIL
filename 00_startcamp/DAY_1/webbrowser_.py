import webbrowser # 선언은 쓰는 시점보다 앞에 와야한다.

keywords = [
    '햄버거 맛집',
    '돈까스',
    '주식정보'
]

for keyword in keywords :
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)

