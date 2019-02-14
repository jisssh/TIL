import sys
sys.stdin = open("input1.txt", "r")
sys.stdout = open("output.txt", "w")

Test = int(input())
for test_code in range(Test):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split()))
    
    print(N)
    print(arr)