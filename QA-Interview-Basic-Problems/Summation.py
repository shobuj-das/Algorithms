# 1. sum all digits of a number
# 2. sum all numbers in an array
# 3. sum all even and odd numbers
# 4. two sum

def all_digit_sum(number):
    result = 0
    while number > 0:
        reminder = number % 10
        result += reminder
        number //=10
    
    return result

def all_numbers_sum_of_array(arr):
    result = 0
    for x in arr:
        result += x

    return result

def even_odd_sum_of_array(arr):
    sumOfEven = 0
    sumOfOdd = 0
    for x in arr:
        if x%2==0:
            sumOfEven += x
        else:
            sumOfOdd += x
    
    return sumOfEven, sumOfOdd

if __name__== "__main__":
    print(all_digit_sum(12345))
    print(all_numbers_sum_of_array([10,20,3,4,5,6]))
    even, odd = even_odd_sum_of_array([1,2,3,4,5,6,7,8,9])
    print(f"Even={even}\nOdd={odd}")