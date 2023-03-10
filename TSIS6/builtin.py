#Write a Python program with builtin function to multiply all the 
#numbers in a list
def multik(l):
    c = 1
    for i in l:
        c *= i
    return c

l = [1, 2, 3, 4, 5]
print(multik(l), end=" ")

#Write a Python program with builtin function that 
# accepts a string and calculate the number of upper case 
# letters and lower case letters
def case_num(s):
    up, lol = 0, 0
    for i in s:
        j = ord(i)
        if j >= 65 and j <= 90:
            up += 1
        elif j >= 97 and j <= 122:
            lol += 1
    return (up, lol)


s = "NzmLvEeeeeEo"
upper_case_number, lower_case_number = case_num(s)
print(upper_case_number)
print(lower_case_number)

#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = input()
if s == s[::-1]:
    print("Yes")
else:
    print("No")
    
#4
import time 

num = int(input())
timer = int(input())
time.sleep(timer / 1000)
print(pow(num, 1/2))

#5:Write a Python program with builtin function that returns True if all elements of the tuple are true.
some_tuple = (1, 1, 0)
print(all(some_tuple))