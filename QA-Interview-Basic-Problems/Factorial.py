# Factorial using loop 
# Factorial using recursive 

def factorial_using_loop(number):
    result = 1
    for i in range(1,number+1,1):
        result *= i
    return result

def factorial_using_recursive(number):
    if number < 1:
        return 1
    return number * factorial_using_recursive(number-1)

if __name__=="__main__":
    print(factorial_using_loop(9))
    print(factorial_using_recursive(9))