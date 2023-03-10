'''
Python iterators and generators
Create a generator that generates the squares of numbers up to some number N.

Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

Implement a generator that returns all numbers from (n) down to 0.
'''
def gen_square(n: int):
    for i in range(1, n + 1):
        yield i**2
input_upto_n = int(input())
print(*gen_square(input_upto_n))

#input: 5
#output: 0, 2, 4
def generator_even(till_number):
    for i in range(0, till_number + 1):
        if (i % 2) == 0:
            yield i  
till = int(input())
list_yields = [*generator_even(till)]

#third task
def divisible(n):
    div_by_3_4 = [i for i in range(0, n + 1) if i % 3 == 0 and i % 4 == 0]
    return div_by_3_4
till = int(input())
print(*divisible(till))

#fourth task
from math import *
def square(limit1, limit2):
    for i in range(limit1, limit2 + 1):
        # print(i)
        # print(sqrt(i))
        if i / int(sqrt(i)) == int(sqrt(i)):
            yield i
        
lower_bound = int(input())
higher_bound = int(input())
print(*square(lower_bound, higher_bound))

#fifth task
def generator_down(n):
    for i in range(n, -1, -1):
        # print(i)
        yield i
begin_with = int(input())
print(*generator_down(begin_with))
