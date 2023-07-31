
#finding duplicates in a list

some_list = ['a', 'b', 'b', 'c', 'd','f','n','n']

# to find the duplicate entries, we need to create a new list by using 'set' to compare against the original list
unique_chars = set(some_list)

# can create an if statement within the a new variable, duplicates.
# here, we create a for loop to run through each character and an if statement
# to find duplicate values in the original list, some_list (>1)

duplicates = [char for char in unique_chars if some_list.count(char) > 1]

print(duplicates)
