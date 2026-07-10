# Problem Statement:
#
# Given two sorted arrays, merge them into a single sorted array.
#
# Input:
# arr1 = [1,3,5]
# arr2 = [2,4,6]
#
# Output:
# [1,2,3,4,5,6]
# ============================================================



def merge_sorted_arrays(arr1, arr2):
    resutl = []
    arr1_len, arr2_len = len(arr1), len(arr2)
    if arr2_len == 0 or arr1_len == 0:
        return resutl
    
    x=y=0
    
    while x < arr1_len or y < arr2_len:
        if x >= arr1_len:
            for i in range(y,arr2_len):
                resutl.append(arr2[i])
                y += 1
        elif y>= arr2_len:
            for i in range(x, arr1_len):
                resutl.append(arr1[i])
                x += 1
        elif x < arr1_len and arr1[x] < arr2[y]:
            resutl.append(arr1[x])
            x += 1
        else:
            resutl.append(arr2[y])
            y += 1

    return resutl

if __name__=="__main__":
    print(merge_sorted_arrays([1,3,4],[2,5,6]))
    print(merge_sorted_arrays([], []))
    print(merge_sorted_arrays([1], []))
    print(merge_sorted_arrays([], [1]))
    print(merge_sorted_arrays([1], [2]))
    print(merge_sorted_arrays([2], [1]))
    print(merge_sorted_arrays([1,3,5], [2,4,6]))
    print(merge_sorted_arrays([1,2,4], [1,3,4]))
    print(merge_sorted_arrays([-5,-2,0], [-3,-1,2]))
    print(merge_sorted_arrays([1,1,1], [1,1]))
    print(merge_sorted_arrays([10,20,30], [5,15,25]))