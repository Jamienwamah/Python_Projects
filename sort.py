numbers = [10, 4, 6, 1, 7, 2, 5, 3, 8, 9]
#sorting in an ascending order using the first method of sorted () function

sorted_numbers = sorted(numbers)
print(sorted_numbers)

#sorting in a descending order using the first method of sorted() function

sorted_number = sorted(numbers, reverse=True)
print(sorted_number)

#sorting in an ascending order using the second method of sort() function

numbers.sort()
print(numbers)

#sorting in a descending order using the second method of sort() function

numbers.sort(reverse=True)
print(numbers)

#sorting using the custom method of sorted() or list.sort using the key parameter to set elements

people = [("Ada", 20), ("Ann", 30), ("Favor", 25)]

#sorting by age, thereby considering the index of the turple

sorted_people = sorted(people, key = lambda x: x[1])
print(sorted_people)

#sorting by age in decending order using the index of the turple

sorted_persons = sorted(people, key = lambda x: x[1])
print(sorted_persons)

#sorting by name, also considering the index of the turple

sorted_people = sorted(people, key = lambda x: x[0])
print(sorted_people)

#sorting by age in descending order using the index of the turple

sorted_people = sorted(people, key = lambda x: x[0])
print(sorted_persons)