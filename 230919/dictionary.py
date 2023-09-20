# Sorting a dictionary by its keys or values

# a1 = {'a':1, 'b':13, 'd':4, 'c':2, 'e':30}
# a1_sorted_keys = sorted(a1, key=a1.get, reverse=True)
# for r in a1_sorted_keys:
#     print(r, a1[r])

my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

sorted_dict = sorted(my_dict.items(), key=my_dict.get, reverse=True)
# sorted_dict = dict(sorted(my_dict.items(),key=my_dict.get))
print(sorted_dict)