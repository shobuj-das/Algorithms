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


if __name__ == "__main__":
    print(fibonacci(3))