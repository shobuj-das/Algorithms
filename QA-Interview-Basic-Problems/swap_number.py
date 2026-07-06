# Problem Statement

# 1. Write a function that swaps two integer values without using a third variable.
# 2. Write a function that swaps two integer values  using xor operator.

#---- 1 -----------------
def swap_numbers(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(f'a = {a}\nb = {b}')

#---- 2 -----------------
def swap_using_xor(a,b):
    a ^= b
    b ^= a
    a ^= b
    return a,b

if __name__=='__main__':
    swap_numbers(a=4,b=5)
    swap_numbers(-3,7)
    swap_numbers(0,-3)

    a ,b = swap_using_xor(a= 5, b=9)
    print(a,b)