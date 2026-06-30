def find_large_number(arr):
    #assume
    large_number = arr[0]

    for i in range(1,len(arr)):
        if arr[i] > large_number:
            large_number = arr[i]
    
    return large_number

def find_second_large_number(arr):
    #assume 
    large_number = arr[0]
    large_number_index = 0

    for i in range(1, len(arr)):
        if arr[i] > large_number:
            large_number = arr[i]
            large_number_index = i
        
    arr.pop(large_number_index)
    #again assume , [when large number is removed, the second last number become the large number now]
    second_large_number = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > second_large_number:
            second_large_number = arr[i]

    return second_large_number

def finding_large_number_between_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


if __name__=="__main__":
    # print(find_large_number([10,5,7,8,9,61,10,8]))
    # print(find_second_large_number([10,5,7,8,9,65,10,80]))

    print(f"Large number: {(find_large_number([10,5,7,8,9,61,10,8]))}")
    print(f"Second large number: {find_second_large_number([10,5,7,8,9,65,10,80])}")

    # number_list = []
    # x = int(input("Enter a number: "))
    # for i in range(0,x):
    #     number_list.append(int(input()))
    
    # print(f"Large number: {find_large_number(number_list)}")
    # print(f"Second large number: {find_second_large_number(number_list)}")

    print(finding_large_number_between_three(4,6,5))
