my_set = {'January','February','March'}
print(type(my_set))
print(my_set)
for element in my_set:
    print(element)

#Set can not be accessed by index value like list in Python
#Add
my_set.add("April")
print(my_set)

#Remove
my_set.remove("April")
print(my_set)