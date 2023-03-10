'''
Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904
'''
from math import *
input_degree = int(input())
output_radian = (input_degree * pi)/ 180
print(output_radian)

from math import *
input_degree = int(input())
output_radian = radians(input_degree)
print(output_radian)
# 180 - 3.14
# 15 - x

'''
Write a Python program to calculate the area of a trapezoid.

Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
'''
def trapezoid(height: int, base1: int, base2 :int):
    area = (base1 + base2)/2 * height
    print(area)
input_height = int(input("Height: "))
input_base1 = int(input("Base, first value: "))
input_base2 = int(input("Base, second value: "))
trapezoid(input_height, input_base1, input_base2)

# 2nd option
def trapezoid(h, a, b):
    return (a + b)/2 * h
input_list = list(map(int, input().split()))
print(trapezoid(*(input_list)))

'''
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''
import math
def area(sides, length):
    area = (.25 * sides * length**2)/(math.tan(math.pi/sides))
    print("The area of the polygon: ",area)
input_num_sides = int(input("Input number of sides: "))
input_length_sides = int(input("Input length of a side: "))
area(input_num_sides, input_length_sides) # naza silaaaa ya rada za tebya


# roma
import math 

def S(n, a):
    return (n * pow(a, 2)) / (4 * math.tan(math.pi / n))

list_1 = list(map(int, input().split()))

print(S(*list_1))
# sanzhan
import math

def degree_to_radian(l):
    r = math.pi * l / 180
    return r

h = int(input("Height: "))
b1 = int(input("Base 1: "))
b2 = int(input("Base 2: "))
print((b1 + b2) * .5 * h)

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
x = float(.25 * n * l**2 * (math.cos(degree_to_radian(180 / n)) / math.sin(degree_to_radian(180 / n))))
print("Area of parallelogram: {par_square}".format(par_square=x))

l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
print(l * h)

'''
Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
'''
def parallelogram(base:int, height:int):
    area = base * height
    print("Expected Output: ", area)
input_base = int(input("Length of base: "))
input_height = int(input("Height of parallelogram: "))
parallelogram(input_base, input_height)
# sin:
import math
def parallelogram(base:int, height:int, ang):
    area = base * height * math.sin(math.pi * ang / 180 )
    print("Expected Output: ", area)
input_base = int(input("Length of base: "))
input_height = int(input("Height of parallelogram: "))
input_angle = int(input("Angle: "))
parallelogram(input_base, input_height, input_angle)
# sin
from math import *
def parallelogram(base:int, height:int, ang):
    area = .5 * base * height * sin(pi * ang / 180 ) 
    print("Expected Output: ", area)
input_base = int(input("Length of base: "))
input_height = int(input("Height of parallelogram: "))
input_angle = int(input("Angle: "))
parallelogram(input_base, input_height, input_angle)
import math
def S(a, h):
    return a * h
list_input = list(map(int, input().split()))
print(S(*(list_input)))

# import math
# n = int(input("Input number of sides: "))
# l = int(input("Input the length of a side: "))
# # area = (.25 * sides * length**2)/(math.tan(math.pi/sides))
# area = float(.25 * n * l**2 * (math.cos(math.pi/n)) / math.sin(math.pi/n))
# print("Area of parallelogram: {paral_square}".format(paral_square = area))