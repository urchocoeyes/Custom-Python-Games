import os

path_name = "C:\Users\Nazym\hello!"
print('Exist:', os.access(path_name, os.F_OK))
print('Readable:', os.access(path_name, os.R_OK))
print('Writable:', os.access(path_name, os.W_OK))
print('Executable:', os.access(path_name, os.X_OK))