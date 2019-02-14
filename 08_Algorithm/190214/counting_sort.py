K = 4
arr = [0, 4, 1, 3, 1, 2, 4, 1] 
cnt = [0] * (K + 1)
sorted = [0] * len(arr)

# 빈도수 계산
for val in arr:
    cnt[val] += 1

# 누적 빈도수
for i in range(1, K + 1):
    cnt[i] = cnt[i-1] + cnt[i]

for i in range(len(arr)-1, -1, -1):
    cnt[arr[i]] -= 1
    sorted[cnt[arr[i]]] = arr[i]

print(sorted)