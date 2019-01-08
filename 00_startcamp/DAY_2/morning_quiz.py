cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
 }

# 3 도시 별 온도 평균
for city in cities_temp: # 왼손으로 key만 꺼내요
    temperatures = cities_temp[city]
    avg_temp =round(sum(temperatures)/len(temperatures),2)
    #for city,temps in cities_temp.items():
    #items 를 쓰는건 두개의 값(key value)을 받아오기 위해?
    print(city + ': ' +  str(avg_temp))
 #  print{'{0}:{1}'.format(city, avg_temp))



# 4 도시중에 최근 3일간 가장 추웠던 곳 , 가장 더웠던 곳
# Hottest : ??, Coldest : ??
# ---밑에꺼는 망한거,,,!---
# coldest = []
# hottest = []


#     for city,temp in cities_temp.items():
#         cold_city = min(temp)
#         coldest.append(cold_city)

#         hot_city = max(temp)
#         hottest.append(hot_city)
    
# print(min(coldest))

# 선생님 답
# all_temp 모든 기온을 모은다.
all_temp = []
for key,value in cities_temp.items():
    all_temp += value
#print(all_temp)

# all_temp 에서 최대/최소를 찾는다.
highest = max(all_temp)
lowest = min(all_temp)

# cities_temp 에서 최대/최소 가 속한 도시를 찾는다.
hottest = []
coldest = []
for key, value in cities_temp.items():
    if highest in value:
       hottest.append(key)

    if lowest in value:
        coldest.append(key)

print(hottest,coldest)