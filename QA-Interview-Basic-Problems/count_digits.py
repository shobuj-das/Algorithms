def count_digits(number):
    counter = 0
    if number == 0:
        counter = 1
        return counter
    while number > 0:
        number //= 10
        counter += 1
    return counter

def count_digits_converting_by_string(number):
    number = str(number)
    return len(number)

if __name__=="__main__":
    print(count_digits(1340090))
    print(count_digits_converting_by_string(103839))