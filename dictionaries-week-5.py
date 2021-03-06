# Dictionaries
# >>>purse = dict()​
# >>>purse['money'] = 12​
# >>>purse['candy'] = 3​
# >>>purse['tissues'] = 75​
# >>>print(purse)​
# {'money': 12, 'tissues': 75, 'candy': 3}​
# >>>print(purse['candy'])​
# 3​
# >>>purse['candy'] = purse['candy'] + 2​
# >>>print(purse)​
# {'money': 12, 'tissues': 75, 'candy': 5}

# Comparing Lists and Dictionaries
    # Lists
    # >>> lst = list()​
    # >>> lst.append(21)​
    # >>> lst.append(183)​
    # >>> print(lst)​
    # [21, 183]​
    # >>> lst[0] = 23​
    # >>> print(lst)​
    # [23, 183]​

    # Dictionaries
    # >>> ddd = dict()​
    # >>> ddd['age'] = 21​
    # >>> ddd['course'] = 182​
    # >>> print(ddd)​
    # {'course': 182, 'age': 21}​
    # >>> ddd['age'] = 23​
    # >>> print(ddd)​
    # {'course': 182, 'age': 23}

# Dictionary Literals (Constants)
# Dictionary literals use curly braces and have a list of key : value pairs​
# You can make an empty dictionary using empty curly braces​
# >>> jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}​
# >>> print(jjj)​
# {'jan': 100, 'chuck': 1, 'fred': 42}​
# >>> ooo = { }​
# >>> print(ooo)​
# {}​
# >>>​

# Counting in a dictionary
# >>> ccc = dict()​
# >>> ccc['csev'] = 1​
# >>> ccc['cwen'] = 1​
# >>> print(ccc)​
# {'csev': 1, 'cwen': 1}​
# >>> ccc['cwen'] = ccc['cwen'] + 1​
# >>> print(ccc)​
# {'csev': 1, 'cwen': 2}​

# Tracebacks in Dictionary
# >>> ccc = dict()​
# >>> print(ccc['csev'])​
# Traceback (most recent call last):​
# File "<stdin>", line 1, in <module>​
# KeyError: 'csev'​
# >>> 'csev' in ccc​
# False​

# Couting a name with Dictionary
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']​
# for name in names :​
#     if name not in counts: ​
#        counts[name] = 1​
#     else :​
#         counts[name] = counts[name] + 1​
# print(counts)

# The get method for dictionaries
# x = counts.get(name, 0)

# Simplified count get method
# counts = dict()​
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']​
# for name in names :​
#     counts[name] = counts.get(name, 0) + 1​
# print(counts)

# Counting Pattern
# The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently.​
# counts = dict()​
# print('Enter a line of text:')​
# line = input('')​
# words = line.split()​
# print('Words:', words)​
# print('Counting...')​
# for word in words:​
#     counts[word] = counts.get(word,0) + 1​
# print('Counts', counts)​

# Definite Loops and Dictionaries​
# Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and looks up the values​
# >>> counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}​
# >>> for key in counts:​
# ...     print(key, counts[key])​
# ... ​
# jan 100​
# chuck 1​
# fred 42​
# >>>

# Retrieving lists of keys and values
# >>> jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}​
# >>> print(list(jjj))​
# ['jan', 'chuck', 'fred']​
# >>> print(jjj.keys())​
# ['jan', 'chuck', 'fred']​
# >>> print(jjj.values())​
# [100, 1, 42]​
# >>> print(jjj.items())​
# [('jan', 100), ('chuck', 1), ('fred', 42)]​
# >>> ​

# Two iteration variables in dictionaries
# jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}​
# for aaa,bbb in jjj.items() :​
#     print(aaa, bbb)
# The following is the outupt of above program
# jan 100​
# chuck 1​
# fred 42

# BigWord and BigCount - Count the biggest word and its frequency in a File
# name = input('Enter file:')
# handle = open(name)
# counts = {}
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1
# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)

# Assignment 9.4 which needs mbox-short.txt
# name = input("Enter file:")
# handle = open(name)
# text = handle.read()
# senders = dict()
# for line in handle:
#     if not line.startswith("From:"):continue
#     line = line.split()
#     line = line[1]
#     senders[line] = senders.get(line, 0) +1
# bigcount = None
# bigword = None
# for word,sender in senders.items():
#     if bigcount == None or sender > bigcount:
#         bigword = word 
#         bigcount = sender 
# print (bigword, bigcount)