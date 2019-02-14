arr = [55, 7, 78, 12, 42]

def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(Bubble_sort(arr))