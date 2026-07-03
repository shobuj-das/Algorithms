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
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    return finding_fibonacci_series_using_recursion(number-1) + finding_fibonacci_series_using_recursion(number-2)

if __name__ == "__main__":
    print(fibonacci(10))

    fib_series = []
    n_terms = 10
    for x in range(n_terms):
        fib_series.append(finding_fibonacci_series_using_recursion(x))
    print(fib_series)