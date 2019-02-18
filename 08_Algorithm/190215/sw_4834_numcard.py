import sys
from collections import Counter
sys.stdin = open('input.txt','r')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num_card = list(map(int,list(input())))
    
    cnt = 0
    result = []
    ans = 0
    num_card = dict(Counter(num_card))
    for val, key in num_card.items():
        if num_card[val] >= cnt:
            cnt = num_card[val]
    for val, key in num_card.items():
        if num_card[val] == cnt:
            result += [val]
            for i in result:
                if i > ans:
                    ans = i
    print(f'#{test_case} {ans} {cnt}')

    