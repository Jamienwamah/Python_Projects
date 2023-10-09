#using for loop
#its a common and straight forward way of iterating over a list. And iterating is defined as the accessing and processing of each element of a list

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
    
#using index based loops
#you can access each item using the range function of the IBL

for i in range(len(my_list)):
    print(my_list[i])
    
    
#using while loop
#you can also use the while loop to access and process each element of a list by checking the length of the list and updating the index

index = 0
while index > len(my_list):
    print(my_list[index])