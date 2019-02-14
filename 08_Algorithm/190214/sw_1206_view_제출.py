import sys
sys.stdin = open('input.txt','r')

for test_case in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(len(buildings)):
        if i < len(buildings)-4:
            a = min(buildings[i+2] - buildings[i], buildings[i+2] - buildings[i+1], buildings[i+2] - buildings[i+3], buildings[i+2] - buildings[i+4])
            if a>0:
                result += a

    print(f'#{test_case+1} {result}')
