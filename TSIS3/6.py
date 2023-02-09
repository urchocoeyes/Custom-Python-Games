def revers(s):
    r = list(s.split(" ")) # or just s.split()
    print(" ".join(reversed(r)))


s = input()
revers(s)