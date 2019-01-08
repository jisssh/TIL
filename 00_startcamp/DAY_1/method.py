my_list = [4, 7, 9, 1, 3, 6]
# 최대 / 최소
max(my_list)
min(my_list)
# 특성 요소의 인덱스?
my_list.index()
# 리스트를 뒤집으려면?
my_list.reverse()

dust = 100 # type <class : int>
lang = 'python' # type <class : str>

samsung = ['elec','sds', 's1'] # type <class : list>
samsung.index('sds') # 1 이 나온다.
samsung.count('s1') # 1 이 니온다.

lang.capitalize() # 처음 p를 대문자로 만들어 준다.
lang.replace('on', 'off') # on이라는 문자가 있으면 off로 대체하라
# 그렇다고 본래의 lang은 바뀌지 않는다는 것을 알아둬!

# samsung.sort() 
# 이거슨 원본이 바뀐다 samsung['elec', 's1', 'sds']

 numbers = [9,5,8,1,2]
 sorted_numbers = numbers.sort()
 sorted_numbers
 numbers # 결과가 [1,2,5,8,9] 로 나온다.

 samsung.append('bio') # 이것도 원본이 바뀐다.
 