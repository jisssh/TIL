team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500
]
# len(team) == 6

type(team[2:4]) # List로 나옴 slicing[2:4] 하면 ['neo']이렇게 나오고
                # team[2]면 'neo'로 나온다

new_member = ['js',10]

team = team + new_member # team += new_member
# 그러면 원래 list team에 새로운 list new_member추가

# len(team) == 8

del(team[2]) # neo가 사라져'
del(team[2]) # 100이 사라져
# len(team) == 7

del(team[2:4])
# len(team) == 4