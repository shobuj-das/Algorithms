# 1. Fiding the largest number from an array
# 2. Finding the second largest number from an array
# 3. Finding largest number among theree numbsers
# 4. Finding largest number among theree numbsers using ternary operator
#===================================================================================

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
        
    arr[large_number_index] = -99999
    #again assume , [when large number is removed, the second last number become the large number now]
    second_large_number = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > second_large_number:
            second_large_number = arr[i]

    return second_large_number

def second_large_number_without_array_modify(arr):
    first_large = None
    second_large =  None

    for num in arr:
        if first_large is None:
            first_large = num
            continue
        elif num > first_large:
            second_large = first_large
            first_large = num
        elif num < first_large:
            if second_large is None:
                second_large = num
                continue
            elif num > second_large:
                second_large = num
    
    return second_large



def finding_large_number_between_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def finding_large_number_between_three_using_ternary_operator(a,b,c):
    largest = a if(a>=b and a>=c) else(b if b>=a and b>=c else c)
    return largest

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

    print(finding_large_number_between_three(5,5,4))
    print(finding_large_number_between_three_using_ternary_operator(5,5,4))
  
    print(second_large_number_without_array_modify([]))
    print(second_large_number_without_array_modify([5]))
    print(second_large_number_without_array_modify([5, 5]))
    print(second_large_number_without_array_modify([-10, -5, -20]))
    print(second_large_number_without_array_modify([-5, -10]))
    print(second_large_number_without_array_modify([10, 20, 5, 15, 25]))
