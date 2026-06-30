def fibonacci(n):
    if n<0:
        raise ValueError("n must be non-negative")
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n==0:
        return [0]
    if n==1:
        return [0]
    
    fib_list = [0,1]
    for i in range(2,n):
        fib_list.append(fib_list[-1]+fib_list[-2])

    return fib_list

def finding_fibonacci_series_using_recursion(number):
    if number < 0:
        raise ValueError("Given number should be non-negative")
    if not isinstance(number, int):
        raise ValueError("number must be an interger")
    if number == 0 or number == 1:
        return 0
    
    print()

if __name__ == "__main__":
    print(fibonacci(3))