# import sys
# sys.stdin = open("input1.txt", "r") # 이 두 줄로 인풋값이 저장되어 있는 텍스트파일 가져와서 인풋 입력 . 단 같은 경로에 있어야 함or 경로지정
# sys.stdout = open("output.txt", "w") # 화면에 출력안되고 이 파일이 생성이 된다.

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print(N)
#     print(arr)

# buildings = ' '.join(input).split()
buildings = [0, 0, 3, 5, 2, 4, 9, 0, 6, 4, 0, 6, 0, 0]
result = 0
for i in range(len(buildings)):
    if i < len(buildings)-4:
        a=(buildings[i+2] - buildings[i])
        b=(buildings[i+2] - buildings[i+1])
        c=(buildings[i+2] - buildings[i+3])
        d=(buildings[i+2] - buildings[i+4])
        if min(a, b, c, d)>0:
            result += min(a, b, c, d)

print(result)
