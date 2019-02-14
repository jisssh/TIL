arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
maxH = 0
for i in range(0, 100):
    height = len(arr)-1-i
    cnt = 0
    for j in range(i+1, len(arr)):
        if arr[i] <=arr[j]: cnt += 1
    height -= cnt
    maxH = max(height, maxH)

print(maxH)