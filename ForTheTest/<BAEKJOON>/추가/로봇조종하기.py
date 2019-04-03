n,m = map(int,input().split())
a = [0] + [[0]+list(map(int,input().split())) for _ in range(n)]
d = [[[-100000000]*3 for j in range(m+2)] for i in range(n+1)]
d[1][1][1] = a[1][1]
for j in range(2, m+1):
    d[1][j][1] = d[1][j-1][1] + a[1][j]
for i in range(2, n+1):
    for j in range(1, m+1):
        d[i][j][0] = max((d[i-1][j][0], d[i-1][j][1], d[i-1][j][2])) + a[i][j];
        d[i][j][1] = max(d[i][j-1][0], d[i][j-1][1]) + a[i][j]
    for j in range(m, 0, -1):
        d[i][j][2] = max(d[i][j+1][0], d[i][j+1][2]) + a[i][j]
print(max(d[n][m]))
