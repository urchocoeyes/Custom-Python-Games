import os

with open(r"nazym.txt", 'r') as f:
    x = len(f.readlines())
f.close()
print("Number of lines of this file: {line_counter}".format(line_counter=x))