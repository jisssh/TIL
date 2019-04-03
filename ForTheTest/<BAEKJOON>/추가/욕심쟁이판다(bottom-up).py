dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
b = []
for i in range(n):
    for j in range(n):
        b.append((i,j,a[i][j]))
b.sort(key=lambda val: -val[2])
for x,y,val in b:
    d[x][y] = 1
    for k in range(4):
        nx,ny =x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if a[x][y] < a[nx][ny]:
                d[x][y] = max(d[x][y],d[nx][ny]+1)
ans = 0
for i in range(n):
    ans = max(ans, max(d[i]))
print(ans)