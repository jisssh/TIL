# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : real & my 가 5개가 같고, my의 나머지 하나가 bonus_number
# 3등 : real & my 가 5개가 같다.
# 4등 : real & my 가 4개가 같다.
# 5등 : real & my 가 3개가 같다.
my_numbers = [1,2,3,4,5,7]
#my_numbers = random.sample(numbers,6)
real_numbers = [1,2,3,4,5,6]

bonus_number = 7

find_rank = list(set(my_numbers).intersection(real_numbers))

if len(find_rank) == 6:
    print('1등입니다.')
elif len(find_rank) == 5:
    if bonus_number in my_numbers and len(find_rank)==5:
        print('2등입니다.')
elif len(find_rank) == 5:
    print('3등입니다.')
elif len(find_rank) == 4:
    print('4등입니다.')
elif len(find_rank) == 3:
    print('5등입니다.')
else:
    print('다음번을 노리세요.')


# 선생님 답_1
count = 0
for my_number in my_numbers:
    for real_number in real_numbers:
        if  my_number ==real_number:
            count += 1

if count ==6:
    print(1)
elif count == 5 and bonus_number in my_numbers:
    print(2)
elif count == 5:
    print(3)

# 선생님 답_2

# match_count  =len(my_numbers & real_numbers)
# print(match_count)

# if match_count==6:
#     print('1등')
# --------------------------------------
#     위와 같다.