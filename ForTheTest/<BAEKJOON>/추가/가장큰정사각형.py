n, m = map(int,input().split())
a = [0] + [[0] + list(map(int,list(input()))) for _ in range(n)]
ans = 0
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i][j] == 0:
            continue
        d[i][j] = min((d[i-1][j-1], d[i-1][j], d[i][j-1])) + 1
        if ans < d[i][j]:
            ans = d[i][j]
print(ans*ans)