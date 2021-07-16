#Create an empty set
s = set()

#Add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

#set values are unique. So even if you add the same number, it will not show as an extra element
s.add(1)

print(s)

#remove a number from set
s.remove(2)
print(s)

#length function
print("There are", len(s), "elements in the set after removing")