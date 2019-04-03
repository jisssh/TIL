n = int(input())
n -= 2
n //= 2
bottom = [-1]*n
hole = [False]*n
top = [0]*n
width = [0]*n
d = dict()
x,y = map(int,input().split())
for i in range(n):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    bottom[i] = y1
    width[i] = (x2-x1)
    d[x2] = i
x,y = map(int,input().split())
m = int(input())
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    index = d[x2]
    hole[index] = True
for i in range(n):
    if hole[i] == False:
        continue
    surface = bottom[i]
    for j in range(i, -1, -1):
        surface = min(surface, bottom[j])
        top[j] = max(top[j], surface)
    surface = bottom[i]
    for j in range(i+1, n):
        surface = min(surface, bottom[j])
        top[j] = max(top[j], surface)
ans = 0
for i in range(n):
    if bottom[i] > top[i]:
        ans += (bottom[i]-top[i])*width[i]
print(ans)
