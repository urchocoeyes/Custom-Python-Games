import os   

path = str(input("ENTER THE PATH TO THE FILE: "))

if not os.path.exists(path):
    print("SOrry, does not exists a file")
    exit(0)

os.remove(path)