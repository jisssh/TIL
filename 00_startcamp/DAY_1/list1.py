numbers = [1, 2, 3] # 변수 이름은 뜻을 담아서 짓자구!
family = ['mom', 1.55,'dad', 1.82,'sis', 1.61]
family[-1] # 마지막

mcu = [
    ['ironman','captain america','dr.strange'],
    ['xmen','deadpool'],
    ['spiderman']
] # 띄어쓰기를 활용하면 보기 편해!
disney = mcu[0]
disney[2] # dr.strange 만 꺼내고 싶을때
# 리스트 안에 리스트 들어간 것을 2차원 리스트라고 한다.
# 만약 그 안에 또 들어가면 3차원 리스트
mcu[0][2] # 랑 위랑 같은 의미임
disney[2] ==mcu[0][2] # True 나옴

iron=['iron'+'man'] # iron = [ironman]

numbers=list(range(1,46))

['a', 'b', 'c', 'c']

int('123') 

bool(1) # True
bool(0) # False
numbers=list(range(100))
numbers[5:10] # 5번째 포함 10번째 제외! (5부터 9까지)
x=['life', 'is', 'short', True, 123, ['you', 'need', 'python']]
# bool 값을 나오게 하고 싶으면?
my_bool = x[3]
my_bool = x[3:4] # or x[-3]