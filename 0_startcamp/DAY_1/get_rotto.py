import requests

url = 'http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
# print(response.text) # type str
lotto_data = response.json() #type dic

real_numbers = []

# for key in lotto_data:
#         if 'drwtNo' in key:
#            real_numbers.append(lotto_data[key])

for Key, value in lotto_data.items():
    if 'drwtNo' in Key:
        real_numbers.append(value)

real_numbers.sort()
bonus)number = lotto_data['drwtNo']
print(real_numbers)


# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5']
# ]
#print(real_numbers)