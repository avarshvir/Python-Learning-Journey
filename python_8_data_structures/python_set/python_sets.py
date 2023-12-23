#create sets
a_sets = {1,2,3,'a',3}
print(a_sets)

#adding element
a_sets.add('B')
print(a_sets)

#length
print(len(a_sets))

#removing element
a_sets.remove(3)
a_sets.discard(3)
print(a_sets)

#union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
# or
union_set = set1 | set2
print(union_set)

#intersection
intersection_set = set1.intersection(set2)
# or
intersection_set = set1 & set2
print(intersection_set)

#difference
difference_set = set1.difference(set2)
# or
difference_set = set1 - set2
print(difference_set)

#symmetric
symmetric_difference_set = set1.symmetric_difference(set2)
# or
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)

# In-place union
print(set1.update(set2))  # Equivalent to set1 |= set2

# In-place intersection
print(set1.intersection_update(set2))  # Equivalent to set1 &= set2

# In-place difference
print(set1.difference_update(set2))  # Equivalent to set1 -= set2

# In-place symmetric difference
print(set1.symmetric_difference_update(set2))  # Equivalent to set1 ^= set2

#clearing set
print(set1.clear())
del a_sets
#print(a_sets)
