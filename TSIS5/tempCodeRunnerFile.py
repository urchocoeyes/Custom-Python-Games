'''
# Python RegEx exercises
# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

# Write a Python program to find sequences of lowercase letters joined with a underscore.

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

# Write a python program to convert snake case string to camel case string.

# Write a Python program to split a string at uppercase letters.

# Write a Python program to insert spaces between words starting with capital letters.

# Write a Python program to convert a given camel case string to snake case.
# '''
# #first task
# import re
# input_str = str(input("Enter a string to check: "))
# pattern = r".*a(b.*)"
# if re.search(pattern, input_str):
#     print("YEES")
# else:
#     print("NOOO")
    
# #second task
# import re
# pattern = r"a(b{2}|b{3})$"
# input = input("после а 2 или 3 раза? ")
# if re.search(pattern, input):
#     print("matched")
# else:
#     print("no bro no")
    