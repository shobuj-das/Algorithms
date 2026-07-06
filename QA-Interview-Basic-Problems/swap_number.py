# Problem Statement

# Write a function that swaps two integer values without using a third variable.

def swap_numbers(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(f'a = {a}\nb = {b}')

if __name__=='__main__':
    swap_numbers(a=4,b=5)
    swap_numbers(-3,7)
    swap_numbers(0,-3)
    
