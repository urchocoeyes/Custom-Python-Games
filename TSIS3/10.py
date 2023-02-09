def uniq(s):
    l = list()
    for i in s:
        if i not in l:
            l.append(i)
    print(l)


s = input() # 6 6 5 1 6
s = s.split()
uniq(s) # ['6', '5', '1']