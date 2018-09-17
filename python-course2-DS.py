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
# print(x)
# y = text.find('5')
# print(y)
# z = text[x : y+1]
# print(float(z))

# File handle as a sequence
# xfile = open('mbox.txt')
# for line in xfile:
#     print(line)

# Couting lines in file
# xfile = open('mbox.txt')
# count = 0
# for line in xfile:
#     count = count + 1
# print(count)

# Reading the whole file
# xfile = open('mbox.txt')
# input = xfile.read()
# print(len(input))
# print(input[:5])

# Searching through a file
# xfile = open('mbox.txt')
# for line in xfile:
#     if line.startswith('String'):
#         print(line)

# Searching through a file and stripping new lines
# xfile = open('mbox.txt')
# for line in xfile:
#     line = line.rstrip()
#     if line.startswith('String'):
#         print(line)

# Enter a file and count the lines
# fname = input('Enter the file name:  ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('String') :
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# Skipping with continue
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:') :
#         continue
#     print(line)

# Using in to select lines
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line : 
#         continue
#     print(line)

# Prompt for file name and search the line starting with
# fname = input('Enter the file name:  ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:') :
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# Bad file names error handling
# fname = input('Enter the file name:  ')
#   try:
#       fhand = open(fname)
#   except:
#       print('File cannot be opened:', fname)
#       quit()

#   count = 0
#   for line in fhand:
#       if line.startswith('Subject:') :
#           count = count + 1
#   print('There were', count, 'subject lines in', fname)

# File Handle
# fhand = open('mbox.txt')
# print(fhand)


# Assignment 7.1 which needs words.txt
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     line = line.rstrip()
#     print(line.upper())

# Assignment 7.2 which needs mbox-short.txt
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# test = 0
# for line in fh:
#     if line.startswith('X-DSPAM-Confidence:'):
#         line = line.rstrip()
#         count = count + 1
#         # print(line)
#         numbers = line[20:]
#         # print(numbers)
#         ppp = float(numbers)
#         # print(ppp)
#         test = test + ppp
#         # print(type(ppp))
# print('Average spam confidence:',test/count)       
# # print(count)

#Final Assignment 7.2 another method using 'if not':
# fn = input("Enter the file name: ")
# fh = open(fn,'r')
# count = 0
# add = 0.0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence") : continue
#     count = count + 1
#     n = (line.rstrip()[19:])
#     add = add + float(n)

# print('Average spam confidence:',add/count)








