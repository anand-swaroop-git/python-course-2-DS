# String as array
# fruit = 'banana'
# x = fruit[0]
# print(x)

#String regex or computations in array
# y = 3
# fruit = 'abcdefg'
# x = fruit[y - 1]
# print(x)

# Finding the length of the string using len function
# fruit = 'banana'
# x = print(len(fruit))

# Looping through strings
# userinput = input('Please enter the string: ')
# try:
#     test = float(userinput)
#     print('Please enter a string and not a number!')
# except:
#     string = userinput
#     index = 0
#     length = len(userinput)
#     while index < length:
#         print(index, string[index])
#         index = index + 1

# Looping through strings
# fruit = 'pineapple'
# for letter in fruit:
#     print(letter)

# Looping and Counting letters in a word
# word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
# count = 0
# for x in word:
#     count = count + 1
# print(count)

# Looping and Counting a particluar letter in a word
# word = 'banana'
# count = 0
# for x in word:
#     if x == 'a':
#         count = count + 1
# print(count)

# Slicing Strings
# s = 'Absolutely Awesome'
# print(s[0:4])
# print(s[4:10])
# print(s[11:20])

# We sometimes omit the starting number and the ending number while slicing the string
# print(s[:4])
# print(s[4:])
# Print whole string:
# print(s[:])

# Using in as a logical operator
# x = 'elephant'
# if 'asd' in x:
#     print('Found it!')
# else:
#     print('Not present!')

# String Library
# greet = 'Hello Bob'
# x = greet.lower()
# print(x)

# print('Hi There!'.lower())

# Finding a method in the classes
# type(4)
# This gives the output <class 'int'>
# Now we check the methods available in int class
# dir(int)
# To check the methods in 'str' class, type this:
# dir(str)

# Common methods examples
    # Searching a string
# fruit = 'banana'
# pos = fruit.find('na')
# print(pos)
# The above program returns the index number of the searched string and in the case above, the output is 2.
# If the string which you have searched for using the find method is not present, you will see a -1 output.

# Search and Replace
# greet = 'Hello Bob'
# nstr = greet.replace('Bob','Jane')
# ppp = greet.replace('o','X')
# print(nstr)
# print(ppp)

# Stripping white spaces
# greet = '   Hello   Bob  '
# print(greet)
# print(greet.lstrip())
# print(greet.rstrip())
# print(greet.strip())

# Prefixes
# line = 'Please have a nice day'
# x = line.startswith('Please')
# x = line.startswith('p')
# print(x)

# Parsing and Extracting | chopping the email address
# x = 'from prasad.testing@google.co.in with something'
# print(x)
# s = x.find('@')
# print(s)
# z = x.find(' ',s)
# print(z)
# tt = x[s+1 : z]
# print(tt)

# Assignment 6.5
# text = "X-DSPAM-Confidence:    0.8475";
# x = text.find('0')
# # print(x)
# y = text.find('5')
# # print(y)
# z = text[x : y+1]
# print(float(z))


















