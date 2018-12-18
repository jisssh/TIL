from darksky import forecast

multicampus = forecast('398869ed5cf60f70dff5d05b3cfafea8',37.501326, 127.039669)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])

# import requests

# url = 'https://api.darksky.net/forecast/398869ed5cf60f70dff5d05b3cfafea8/37.501309,%20127.039713'

# res = requests.get(url)
# data = res.json()

# print(data['currently']['summary'])
# 주석 처리 한것과 성능 차이는 없지만 뭔가
# 부가적인 일을 하는 느낌이라...