import sys
sys.stdin = open('input.txt','r')

for test_case in range(1, 11):
    N = int(input())
    flatten = list(map(int,input().split()))

    min_num = 101
    max_num = 0
    max_idx = -1
    min_idx = -1
    for i in range(len(flatten)):
        if flatten[i] > max_num:
            max_num = flatten[i]
            max_idx = i  
        if flatten[i] < min_num:
            min_num = flatten[i]
            min_idx = i

    while N != 0:
        flatten[max_idx] = flatten[max_idx] - 1
        flatten[min_idx] = flatten[min_idx] + 1
        min_num = 101
        max_num = 0
        max_idx = -1
        min_idx = -1
        for i in range(len(flatten)):
            if flatten[i] > max_num:
                max_num = flatten[i]
                max_idx = i  
            if flatten[i] < min_num:
                min_num = flatten[i]
                min_idx = i
    
        if flatten[max_idx] == flatten[min_idx]:
            N=0
        N -= 1
    result = flatten[max_idx] - flatten[min_idx]  

    print(f'#{test_case} {result}')