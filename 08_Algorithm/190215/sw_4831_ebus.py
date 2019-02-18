import sys
sys.stdin = open('input.txt','r')
T = int(input())
for test_case in range(1, T+1):
    K,N,M = list(map(int,(input().split())))
    M_list = list(map(int,(input().split())))

    o = K
    d = 0
    cnt = 0
    ans = 0
    result = 1
    M_list += [N]
    for i in range(len(M_list)):
        if i < len(M_list)-1:
            if(M_list[i+1]-M_list[i])> K:
                result = 0
                break;
        else:
            while d < N:
                d += 1
                o -= 1
                if d in M_list and d!=N:
                    for i in range(len(M_list)):
                        if i < len(M_list)-1 and (d == M_list[i]):
                            if o < (M_list[i+1]-M_list[i]) :
                                o = K
                                cnt += 1
                                break;
    if result == 0:
        ans =result
    else:
        ans = cnt

    print(f'#{test_case} {ans}')
    
