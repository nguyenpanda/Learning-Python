test_list = ["ha", 1, 1.9234, [1, 2, 3, 4], {3, 1, 2, 3, 4, 'ha'}, (1, 34, 5, 346, 'ha')]
print("List can contain list, set, tuple -->", test_list)

my_list_1 = [1, 3, 9, 5, 6, 100, 2, 3, 1, 0, 0, 3, 1, 0, 1]

print("Count list -->", my_list_1.count(1))

my_list_1.reverse()
print("Reverse list -->", my_list_1)

my_list_1.sort()
print("Sort list -->", my_list_1)

# my_list_1.append("Ha", "Tuong") wrong because we take exactly one argument
my_list_1.append("Ha")
print("Append list -->", my_list_1)

my_list_1.remove(1)
print("Remove list -->", my_list_1)

my_list_2 = ["He", "Haha", "Fuck"]

my_list_1.extend(my_list_2)
print("Extend list -->", my_list_1)

my_list_1 = my_list_2.copy()
print("Copy list -->", my_list_1)
