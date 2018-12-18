my_info = {
    'name':'Jiss',
    'job':'student',
    'mobile':'01050242683',
    'email':'jisssh@naver.com'
}
my_info['email']

hphk=[
    {
        'name':'john',
        'email':'john@naver.com'
    },
    {
        'name':'neo',
        'email':'neo@naver.com'
    },
    {
        'name':'tak',
        'email':'tak@naver.com'
        'married': False
    }
] # tak의 정보에 접근하려면? 음 특히 tak의 이름!
p = hphk[2]
print(p['name']) # 이거 두개 합치려면 p=hphk[2]['name'] 이렇게 쓸 수 있다.
print(type(p)) # dictionary'

