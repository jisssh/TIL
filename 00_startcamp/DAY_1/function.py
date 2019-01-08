print('hi')
len('hi') # 2
len([1,2,3,4,5]) # 5
del()
type('hi')

scores = [45, 60, 78, 88]
high_score = max(scores)
lowest_score = min(scores)

round(1.8) # = 2 반올림이다. ceil / floor (올림 / 내림)]
round(1.876,2) # = 1.88 두번째 자리 반올림이다.

first = [11, 25, 18.0, 20.0]
second = [10, 75, 9.50]

# full에 first와 second을 합쳐서 저장
full = first + second
# full_sorted에 함수 full을 정렬해서 저장(오름차순)
full_sorted = sorted(full)
# 도전과제! *reverse_sorted에 full을 내림차순으로 정렬해서 저장
reverse_sorted = reversed(full_sorted)
# reverse_sorted = sorted(full, reverse=True)
list(reverse_sorted)