arr = 'ABCD'


for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: continue
        for k in range(len(arr)):
            if k == i or k == j: continue
        print(arr[i], arr[j])