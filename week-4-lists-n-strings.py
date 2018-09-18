# # Lists examples
# friends = ['x', 'y', 'z']
# print(friends,friends[2])

# # List Constants examples
# print(['red', 2, 4])

# # A list can have another list
# print([1, [2, 8], 7])

# # A list can be empty
# print([])

# Range Function
# friends = ['x', 'y', 'z']
# print(len(friends))
# print(range(len(friends)))

# A tale of two loops
# friends = ['Joseph', 'Glenn', 'Sally']

# for friend in friends :
#     print('Happy New Year:',  friend)

# for i in range(len(friends)) :
#     friend = friends[i]
#     print('Happy New Year:',  friend)

# Manipulating Lists
    # Concatenating Lists using +
# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)

# Slicing Lists
t = [9, 41, 12, 3, 74, 15]
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[:])
# print(t[2:4])

# List Methods
# >>> x = list()
# >>> type(x)
# <type 'list'>
# >>> dir(x)
# ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> 

# Building a list from scratch
# >>> stuff = list()
# >>> stuff.append('book')
# >>> stuff.append(99)
# >>> print(stuff)
# ['book', 99]
# >>> stuff.append('cookie')
# >>> print(stuff)
# ['book', 99, 'cookie']

# Is somthing in a list
# >>> some = [1, 9, 21, 10, 16]
# >>> 9 in some
# True
# >>> 15 in some
# False
# >>> 20 not in some
# True
# >>> 

# Sorting the list
# friends = [ 'Joseph', 'Glenn', 'Sally' ]
# friends.sort()
# print(friends)

# Built in functions in lists
# nums = [3, 41, 12, 9, 74, 15]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)/len(nums))

# Finding average using old method (Manual, without using built-in functions)
# total = 0
# count = 0
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value     
#     count = count + 1

# average = total / count
# print('Average:', average)

# Finding the average using built-in functions
# numlist = list()
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average:', average)

# Splitting the strings and converting into lists
# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
# print(len(stuff))
# print(stuff[0])

# #For loop in the above for fun
# print(stuff)
# for w in stuff :
#     print(w)

# Split function with delimiter
# # Without delimiter, split takes more than one space = only one space
# line = 'A lot               of spaces'
# etc = line.split()
# print(etc)

# # After specifying delimiter ; with split function
# line = 'first;second;third'
# thing = line.split(';')
# print(thing)

# Using split to chop email
# fhand = open('mbox-short.txt')
#  for line in fhand:
#      line = line.rstrip()
#      if not line.startswith('From ') : continue
#      words = line.split()
#      print(words[2])

# Using split function to chop split email addresses (Own method)
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From ') : continue
#     words = line.split()
#     x = (words[1].split('@'))
#     print(x[1])

# Assignment 8.4 needs romeo.txt (WIP)
# fname = input("Enter file name: ")
# fh = open(fname)
# stuff = list()
# for line in fh:
#     line = line.rstrip().split()
#     for x in line:
#         if x in stuff: continue
#         else:
#             stuff.append(x)
# # print(stuff)
# stuff.sort()
# print(stuff)

     


    
