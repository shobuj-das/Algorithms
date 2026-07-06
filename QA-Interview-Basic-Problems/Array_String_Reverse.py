# 1. Array reverse 
# 2. String reverse 
# 3. 2D array reverse (transpose matrix)


# ----------- Array Reverse ---------------------------
def array_reverse_using_same_array(arr):
    x = len(arr) - 1
    for i in range(0, len(arr)//2):
        temp = arr[i]
        arr[i] = arr[x]
        arr[x] = temp
        x -= 1

    return arr

def array_reverse_using_second_array(arr):
    rev_arr = []
    x = len(arr) - 1
    for i in range(0,len(arr)):
        rev_arr.append(arr[x])
        x -= 1

    return rev_arr

# ----------- String Reverse ---------------------------
def string_reverse(str):
    x = len(str) - 1
    strList = list(str)
    
    for y in range(0,len(str)//2):
        strList[x], strList[y] = strList[y], strList[x]
        x -= 1
        
    strList = "".join(strList)
    return strList


# ----------- 2D array Reverse ---------------------------
def reverse_print_2D_array(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    print(f'total element in the matrix: {rows * cols}')

    for i in range(cols):
        for j in range(rows):
            print(matrix[j][i],end=" ")
        print("\n")

# ---------- transpose matrix -----------------------
def reverse_2D_array(matrix):
    transposeMatrix = []
    rows = len(matrix)
    cols = len(matrix[0])

    for c in range(cols):
        rowArray = []
        for r in range(rows):
            rowArray.append(matrix[r][c])
        transposeMatrix.append(rowArray)
    
    return transposeMatrix

    
if __name__=="__main__":
    print(array_reverse_using_same_array([1,2,3,4,5,6,7,8,9]))
    print(array_reverse_using_second_array([9,8,7,6,5,4,3,2,1]))
    print(string_reverse("abcdef"))

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(matrix)
    reverse_print_2D_array(matrix)

    transposeMatrix = reverse_2D_array(matrix)
    for row in transposeMatrix:
        print(row)