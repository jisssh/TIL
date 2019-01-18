import requests

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=840'

response = requests.get(URL)

print(response)