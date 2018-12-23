import operator

the_dict = {1: 22, 2: 11, 3: 14, 4: 10, 5: 4, 6: 99, 7: 88}
print("Original Dictionary", the_dict)
sorted_the_dict = sorted(the_dict.items(), key=operator.itemgetter(0))
print("Sorted Dictionary", sorted_the_dict)
sorted_the_dict = sorted(the_dict.items(), key=operator.itemgetter(0), reverse=True)
print("A reversed dictionary", sorted_the_dict)