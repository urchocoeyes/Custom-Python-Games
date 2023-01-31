i = 1 
while i < 6:
    print(i)
    i += 1

#2nd example
i = 1 
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#3rd example
i = 0 
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#4th example
i = 1
while i < 6:
    print(i)
    i += 1 
else:
    print("i is no longer less than 6")

