import sys
sys.stdin = open('input_4835.txt','r')
T = int(input())
for test_case in range(1, T+1):
    N,M = list(map(int,(input().split())))
    part_sum = list(map(int, input().split()))
    sum_result = 0
    min_result = 999999999
    max_result = 0

    for i in range(len(part_sum)-M+1):  
        for j in range(M):
            sum_result += part_sum[j+i]
        if sum_result < min_result:
            min_result = sum_result
        if sum_result > max_result:
            max_result = sum_result
        sum_result = 0
    result = max_result-min_result
    print(f'#{test_case} {result}')
