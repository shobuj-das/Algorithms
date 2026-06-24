def remove_duplicate_using_second_array(arr):
    new_arr = []
    for x in range(0, len(arr)):
        if arr[x] not in new_arr:
            new_arr.append(arr[x])

    print(new_arr)

def remove_duplicate_from_same_array(arr):
    for x in range(0, len(arr)):
        j = x +1
        while j < len(arr):
            if arr[x] == arr[j]:
                arr.pop(j)
            else:
                j+=1
    
    print(arr)
                

if __name__=="__main__":
    remove_duplicate_from_same_array([10,5,7,9,5,4,1,3,2,4,4,5,5,5,5,8])
    remove_duplicate_using_second_array([1,2,3,5,4,8,5,2,3,2,5,4,4,4,7,7,1,2])
