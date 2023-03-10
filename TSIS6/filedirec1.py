import os
f = open("nazym.txt", "w")
l = os.listdir(r"C:\Users\Nazym\hello!\TSIS6")
# print(l)
text = '\n'.join(l)
print(text)
f.write(text)

