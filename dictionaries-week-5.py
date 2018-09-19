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