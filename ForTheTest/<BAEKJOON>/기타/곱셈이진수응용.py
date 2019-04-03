def mul(a, b, c):
    ans = 1
    while b > 0:
        if b%2 == 1:
            ans *= a
            ans %= c
        b //= 2
        a *= a
        a %= c
    return ans

a,b,c = map(int,input().split())
print(mul(a,b,c))
