#unpacking deals with extracting of individual element and assigning them a variable

#Basic unpacking

my_list = [1, 2, 3]
a, b, c = my_list

print(a)
print(b)
print(c)

#Extended unpacking
#Using the * operator to unpack the remaining elements of a list

my_list = [1, 2, 3, 4, 5, 6]
a, *rest = my_list

print(a)
print(rest)

#swapping variables
#unpacking the commonly used for variable without the need for temporary variables

a = 1
b = 2
a, b = b, a
print(a)
print(b)

#ignoring values
#you can use '_' to ignore certain values during unpacking whe you are not interested in them

my_list = [1, 2, 3, 4, 5]

a, _, c, *rest = my_list
print(a)
print(c)
print(rest)
