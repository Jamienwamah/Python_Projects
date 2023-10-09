numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#to slice from the index to the end(inclusive)

sliced_numbers = numbers[3:]
print(sliced_numbers)

#to slice from the beginning to the index(exclusive)

sliced_number = numbers[:3]
print(sliced_number)

#multiple slicing 
sliced_multiple = numbers[2:5:9]
print(sliced_multiple)
 
#to omit an index that is to copy the entire list
sliced_omit = numbers[:]
print(sliced_omit)


my_list = ["I", "Love", "Favor"]

sliced_list = my_list[1:]
print(sliced_list)

sliced_lists = my_list[:1]
print(sliced_lists)