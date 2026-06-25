import math

def is_prime_numbers(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    
    return True

if __name__== "__main__":
    rangeFrom = int(input("Enter range from:"))
    rangeTo = int(input("Enter range to: "))
    for i in range(rangeFrom, rangeTo):
        if is_prime_numbers(i):
            print(i)
