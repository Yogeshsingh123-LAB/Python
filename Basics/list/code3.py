'''the append() method. This is used to add an item to the end of 
the list. Here is an example of using the append() method to add 
the number 6 to list of numbers:'''

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers)# [1, 2, 3, 4, 5, [6, 8, 10]]

'''The extend() method is similar to the append() method,
   but with extend() you can add multiple elements from one 
   list to another. Here's an example of adding the numbers
   6, 8, and 10 from one list to 
   the end of the numbers list'''

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

''' To insert an element at a specific index in a list, 
you can use the insert() method. This method accepts two arguments: 
the index where you wish to insert the new item and the
item you want to insert.'''

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print(numbers) # [1, 2, 2.5, 3, 4, 5]

'''To remove an element at a specific index in the list, you can use the pop() method'''
numbers = [1, 2, 3, 4, 5]
numbers.pop(2)
print(numbers) # [1, 2, 4, 5]   

'''If you need to empty the list, then you can use the clear() method'''
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers) # []

'''the sort() method. This method is used to sort the elements in place. 
Here is an example of sorting a random list of numbers in place'''
numbers = [5, 2, 9, 1, 3]
numbers.sort()
print(numbers) # [1, 2, 3, 5, 9]

'''the sorted() function which works for any iterable and returns a 
new sorted list instead of modifying the original list.'''
numbers = [5, 2, 9, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # [1, 2, 3, 5, 9]
print(numbers) # [5, 2, 9, 1, 3]

''' the reverse() method. This method, will reverse a list of elements in place'''
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers) # [5, 4, 3, 2, 1]

'''the reversed() function, which returns an iterator that can be used to reverse a list without modifying the original list.'''
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers) # [5, 4, 3, 2, 1]
print(numbers) # [1, 2, 3, 4, 5]

'''the index method. This is used to find the first index where an element can be found in a list'''
numbers = [1, 2, 3, 4, 5]
index_of_3 = numbers.index(3)
print(index_of_3) # 2
