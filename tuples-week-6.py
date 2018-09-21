# Tuples are like lists
# >>> x = ('Glenn', 'Sally', 'Joseph')
# >>> print(x[2])
# Joseph
# >>> y = ( 1, 9, 2 )
# >>> print(y)
# (1, 9, 2)
# >>> print(max(y))
# 9

# Operations possible on Tuple and Lists
# >>> l = list()
# >>> dir(l)
# ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# >>> t = tuple()
# >>> dir(t)
# ['count', 'index']


# Tuple and assignment - We can also put a tuple on the left-hand side of an assignment statement
# We can even omit the parentheses
# >>> (x, y) = (4, 'fred')
# >>> print(y)
# fred
# >>> (a, b) = (99, 98)
# >>> print(a)
# 99

# Tuples and Dictionaries - The items() method in dictionaries returns a list of (key, value) tuples
# >>> d = dict()
# >>> d['csev'] = 2
# >>> d['cwen'] = 4
# >>> for (k,v) in d.items(): 
# ...     print(k, v)
# ...
# csev 2
# cwen 4
# >>> tups = d.items()
# >>> print(tups)
# dict_items([('csev', 2), ('cwen', 4)])

# Tuples are comparable - The comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the next element,  and so on, until it finds elements that differ.
# >>> (0, 1, 2) < (5, 1, 2)
# True
# >>> (0, 1, 2000000) < (0, 3, 4)
# True
# >>> ( 'Jones', 'Sally' ) < ('Jones', 'Sam')
# True
# >>> ( 'Jones', 'Sally') > ('Adams', 'Sam')
# True

# Sorting Lists of Tuples - We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
# - First we sort the dictionary by the key using the items() method and sorted() function
# >>> d = {'a':10, 'b':1, 'c':22}
# >>> d.items()
# dict_items([('a', 10), ('c', 22), ('b', 1)])
# >>> sorted(d.items())
# [('a', 10), ('b', 1), ('c', 22)]

# Using sorted() in a for Loop - Sorting by keys
# >>> d = {'a':10, 'b':1, 'c':22}
# >>> t = sorted(d.items())
# >>> t
# [('a', 10), ('b', 1), ('c', 22)]
# >>> for k, v in sorted(d.items()):
# ...    print(k, v)
# ...
# a 10
# b 1
# c 22

# Sorting by Values in the above
# >>> c = {'a':10, 'b':1, 'c':22}
# >>> tmp = list()
# >>> for k, v in c.items() :
# ...     tmp.append( (v, k) )
# ... 
# >>> print(tmp)
# [(10, 'a'), (22, 'c'), (1, 'b')]
# >>> tmp = sorted(tmp, reverse=True)
# >>> print(tmp)
# [(22, 'c'), (10, 'a'), (1, 'b')]

# Top 10 Most Common Words Program
# fhand = open('romeo.txt')
# counts = {}
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0 ) + 1

# lst = []
# for key, val in counts.items():
#     newtup = (val, key) 
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)

# for val, key in lst[:10] :
#     print(key, val)

# List Comprehension - Even Shorter Version of the above Program - List comprehension creates a dynamic list.  In this case, we make a list of reversed tuples and then sort it.

# >>> c = {'a':10, 'b':1, 'c':22}
# >>> print( sorted( [ (v,k) for k,v in c.items() ] ) )
# [(1, 'b'), (10, 'a'), (22, 'c')]

# Assignment 10.2 which needs mbox-short.txtname = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# counts = dict()
# for line in handle :
# 	line = line.rstrip()
# 	if line == "": continue
# 	words = line.split()
# 	if words[0] != "From" : continue
# 	time = words[5].split(":")
# 	counts[time[0]] = counts.get(time[0], 0) + 1
# list = list()
# for key,value in counts.items() :
# 	list.append((key,value))
# list.sort()
# for hour,count in list :
# 	print(hour, count)