myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) # dublicates will be ignored

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
