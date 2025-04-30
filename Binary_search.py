def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
target = int(input("Enter the element to be searched: "))
result = binary_search(arr, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")