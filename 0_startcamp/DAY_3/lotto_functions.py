import requests
import random
# 인자가 있고 리턴이 있다. / yes in yes out
# 인자가 있도 리턴이 없다. / yes in no out
# 인자가 없고 리턴이 있다. / no in yes out
# 인자가 없고 리턴도 없다. / no in no out

def pick_lotto():
        numbers =random.sample(list(range(1,46)),6)
       #list 라는 말이 없어도 된다.
        return numbers

# print(pick_lotto())


# result= am_i_lucky(my_numbers, real_numbers)

def get_lotto(draw_no):
        url = 'http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(draw_no)
        response = requests.get(url)
        #print(response.text) # type str
        lotto_data = response.json() #type dic

        numbers = []
        # bonus_number = lotto_data['bnusNo']
        # real_numbers = []

    
        for key, value in lotto_data.items():
            if 'drwtNo' in key:
                numbers.append(value)

        numbers.sort()
        bonus_number = lotto_data['bnusNo']
        # { number: [1,2,3,4,5,6], bonus : 7 }
        final_dict = {
            'numbers':numbers,
            'bonus':bonus_number
        }
        return final_dict

# print(get_lotto(833))


def am_i_lucky(pick, draw):

    match_count = len(set(pick) & set(draw['numbers']))

    if match_count==6:
        return('1등입니다.')
    elif match_count == 5:
        if draw['bonus'] in pick and match_count==5:
            return('2등입니다.')
        else:
            return('3등입니다.')
    elif match_count == 4:
        return('4등입니다.')
    elif match_count == 3:
        return('5등입니다.')
    else:
        return('꽝')

result = am_i_lucky(pick_lotto(),get_lotto(833))
print(result)
