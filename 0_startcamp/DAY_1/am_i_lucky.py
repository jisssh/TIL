import requests
import random

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
real_numbers =set(real_numbers)

bonus_number = lotto_data['bnusNo']
print(real_numbers)

# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : real & my 가 5개가 같고, my의 나머지 하나가 bonus_number
# 3등 : real & my 가 5개가 같다.
# 4등 : real & my 가 4개가 같다.
# 5등 : real & my 가 3개가 같다.
match_count  =len(my_numbers & real_numbers)
print(match_count)

if match_count==6:
    print('1등')
elif match_count == 5:
    if bonus_number in my_numbers and match_count==5:
        print('2등입니다.')
elif match_count == 5:
    print('3등입니다.')
elif match_count == 4:
    print('4등입니다.')
elif match_count == 3:
    print('5등입니다.')
else:
    print('다음번을 노리세요.')