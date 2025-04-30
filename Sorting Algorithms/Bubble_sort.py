def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(0, size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(arr))
