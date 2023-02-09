from itertools import permutations

def permut(s):
    l = list(permutations(s))
    print(l) # [('a', ' ', 'b'), ('a', 'b', ' '), (' ', 'a', 'b'), (' ', 'b', 'a'), ('b', 'a', ' '), ('b', ' ', 'a')]
    for i in l:
        print(''.join(i))


s = input()
permut(s)
