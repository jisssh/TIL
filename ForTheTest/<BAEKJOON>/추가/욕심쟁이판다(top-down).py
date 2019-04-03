import sys
sys.setrecursionlimit(2000*2000)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
def go(i, j):
    if d[i][j] != 0:
        return d[i][j]
    d[i][j] = 1
    for k in range(4):
        x,y = i+dx[k], j+dy[k]
        if 0 <= x < n and 0 <= y < n:
            if a[i][j] < a[x][y]:
                d[i][j] = max(d[i][j], go(x,y)+1)
    return d[i][j]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, go(i,j))
print(ans)