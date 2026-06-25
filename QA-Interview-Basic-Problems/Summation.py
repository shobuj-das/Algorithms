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

if __name__== "__main__":
    print(all_digit_sum(12345))