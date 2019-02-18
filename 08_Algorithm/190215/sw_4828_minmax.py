import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    min_max = list(map(int, input().split()))
    min_num = min_max[0]
    max_num = min_max[0]
    for num in min_max:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    result = (max_num-min_num)
    print(f'#{test_case} {result}')