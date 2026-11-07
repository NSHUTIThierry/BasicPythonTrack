
fruit = ["apple", "banana",]
fruit.append("cherry")
print(fruit)
fruit.insert(1, "orange")
print(fruit)
vegetables = ["carrot", "broccoli", "spinach"]
print(vegetables)
copy1=fruit.copy()
print(copy1)
copy2=list(fruit)
print(copy2)
list1 = ["a", "b", "c"]
list2=list([12,23,53])
print(list2)
remove_item = list1.pop(1)
print(remove_item)
fruit.remove("cherry")
print(fruit)
clear_list = vegetables.clear()
print(vegetables)
