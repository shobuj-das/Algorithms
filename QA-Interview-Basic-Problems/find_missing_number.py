# Problem Statement
# Given an array containing numbers from 1 to n, exactly one number is missing.

# Find the missing number.

# Example 1
# Input:
# [1,2,3,5]

# Output:
# 4
# Example 2
# Input:
# [2,3,1,5]

# Output:
# 4


def finding_missing_number(arr):
    found_list = [0] * (len(arr)+1)
    print(found_list)
    for x in arr:
        found_list[x-1] = 1

    missing = 0
    for y in found_list:
        if y == 0:
            missing += 1
            return missing
        missing += 1


def missing_number(arr):
    for x in range(1,len(arr)+1):
        if x not in arr:
            return x
        

if __name__=='__main__':
    arr = []
    n = int(input("Enter n value: "))
    for x in range(n):
        arr.append(int(input()))

    # arr = [1,2,3,4,6]
    print(finding_missing_number(arr))
