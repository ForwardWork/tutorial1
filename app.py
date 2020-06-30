# print("Hello World")
# print("*" * 10)


# print("Hello World")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# 2 + 3


# x = 1
# y = 2
# Unti_Prize = 3
# print(Unti_Prize)
# print(y)
# print(x)

# student_count = 1000  # integer
# rating = 4.99  # float
# is_published = False  # boolean
# course_name = "Python Programming"
# print(student_count)

# print(len(course_name))
# print(course_name[0])
# print(course_name[-1])
# print(course_name[0:3])
# print(course_name[0:])
# print(course_name[:3])
# print(course_name[:])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==

# course = " Python Programming "
# print(course)
# comments \" gives the quotes
# /' adds a single quote to text
# // to include a backlash in text
# \n adds a new line

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# #first = "Janyne"
# last = "Doe"
# full = f"{first} {last}"
# print(full)

# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.rstrip())
# print(course.find("Pro"))  # returns index
# print(course.replace("P", "i"))
# print("Pro"in course)
# print("switft"not in course)

# x = input("x: ")
# print(type(x))
# y = int(x)+1
# print(f"x: {x}, y:{y}")

# temperature = 15
# if temperature > 30:
#     print("its warm")
#     print("drink water")
# elif temperature > 20:
#     print("its nice")
#     pass
# else:
#     print("its cold")
# print("Done")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# age = 13
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")


# age = 22
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

# high_income = False
# good_credit = True
# student = False
# # if high_income or good_credit:
# # if not student:
# # 654Yu7y2if (high_income or good_credit) and not student:
# print("eligible")
# else:
#     print("Not Eligible")


# for number in range(1, 10, 2):
#     print("attempt", number, (number) * ".")

# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("attempted 3 times and failed ")

# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")

# print(type(5))
# print(type(range(5)))

# iterable, range function is iterable

# for x in range(5):
# for x in "python":
#         print(x)

# for x in [1, 2, 3]:
#     print(x)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# while loop repeat as long a condition is true

# number = 100
# while number > 0:
#     print(number)
#     number //= 2


# command = ""
# while command != "quit":
#     command = input(">")
#     print("ECHO", command)


# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower.lower() == "quit":
#         break

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         print(number)
#         count += 1
# print(f"we have {count} even numbers")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# def greet(first_name, last_name):  # use lower case to name fucntions
#     print(f"Hi there {first_name} {last_name}")
#     print("welcome aboard")

#     # 2 line breaks at the end of a function
# greet("Jane", "Jones")
# greet("Peter", "Smitt")


# def greet(name):
#     print(f"Hi {name}")

#     return f"hi {name}"

#     message = get_greeting("Jane")
#     file = open(contenet.txt, "w")
#     file.write(message)

# default arguments
# def increment(number, by):
#     return number + by


# print(increment(2, by=1))
# by can be a optional paramenter

# def increment(number, by=1): # by now has a default of 1 if not called in the call
#     return number + by


#  print(increment(2)) # this will give 3 as the default is used however if 2nd argument is placed in this call say 5 then this will overwrite default resulting in 7
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# # argument collections
# def multiply(*numbers):  # arugment of function indicate a collection or paramenters, a tuple - that cannot be adjusted
#     total = 1
#     for number in numbers:
#         #total = total * numbers
#         total *= number
#     return(total)


# print(multiply(2, 3, 4, 5))

# def save_user(**user):  # permits a list of key value pairs which python turns into a dictionary. this can then be passed over with [] to obtain vale of lable

#     print(user)


# save_user(id=1, name="john", age=22)

# local and global


# def multiply(*numbers):  # debug
#     total = 1
#     for number in numbers:
#         #total = total * numbers
#         total *= number
#     return(total)


# print(multiply(1, 2, 3))
# print("start")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# if no / by 3 print fizz, if no /5 buzz, if no divided by both print fizz buzz, beloe does tihs but not elegantly

# def fizz_buzz_game(input):

#     if input % 3 == 0:
#         print("Fizz")
#     if input % 5 == 0:
#         print("Buzz")
#     # if (input % 3 == 0) & (input % 5 == 0):
#     #     print("FizzBuzz")
#     elif (input % 3 != 0) & (input % 5 != 0):
#         print(input)


# fizz_buzz_game(15)

# # MOSH solution for FizzBuzz


# def fizz_buzz_gameM(input):

#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return"Fizz"
#     if input % 5 == 0:
#         return("Buzz")
#     return(input)


# print(fizz_buzz_gameM(15))
# unpacking items from a list

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# numbers = [1, 2, 3]
# # must have the same number of items on left of = as match the number in the list or it is not possibe to unpack
# first, second, third = numbers

# #  #same as
# #  first = numbers[0]
# #  second = numbers[1]
# #  third = numbers[2]
# # it is possible to pack items from a list where you do not want everything

# numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, ]
# first, second, *others = numbers  # the others item


# letters = ["a", "b", "c"]
# # gives a tuple, list is not changebale but can be iterated over and upacked
# for index, letter in enumerate(letters):
#     print(index, letter)

# letters = ["a", "b", "c"]
# add

# when functionas are part of an object, it is referred to as a method the letters list here is an object (an array list which can be added to)
# letters.append("d")  # adds d to end
# inserts - in index position 0 before 1 shifiting all up
# letters.insert(0, "-")
# remove
# letters.pop()  # will remove the last item in the list
# letters.pop(0)  # will remove the - from list as have indicated index 0

# letters.remove("b")  # will remove the 1st occurance of b
# del letters[0:3]
# letters.clear()
# if "d" in letters:
#     print(letters.index("d"))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# soritng lists

# numbers = ["3", "51", "2", "8", "6"]

# numbers.sort(reverse=True)
# print(sorted(numbers))
# print(numbers)
# numbers = ["3", "51", "2", "8", "6"]

# #numbers.sort(reverse=True)
# print(sorted(numbers))
# print(numbers)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
"""items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


# def sort_item(item):
#     return item[1]


# items.sort(key=lambda item: item[1])
# print(items)

# lambda is argument used as an annonymous function and can rewrite the def function?

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]
# prices = []
# for item in items:
#   prices.append(item[1])

# pricesx = list(map(lambda item: item[1], items))  # same as above for loop

# print(pricesx)
# for item in x:
#   print(item)


# print(x)  # provides an iterrable object address which needs to put iterated over ti pull out the values
# print(prices)


# prices = list(map(lambda: item[1], items))
# is same as above mapping a list from one thing to another
prices = [item[1] for item in items]
# filterd = list(filter(lambda item: [1] >= 10, item

# same as above but cleaner, a new list has been defined and will iterate over itself with the if condition imposed
filtered = [item for item in items if item[1] >= 10]
print(filtered)
"""
# # 2 lists to combine
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# # when combined should see the 1st number of each tuple combined like
# #[(1, 10), (2, 20), (3, 30)]
# # produced an object location which is iterrable, and can be pushed to a list function to see contents
# print(list(zip(list1, list2)))

# # as possible for the object to take any item we can add the following
# print(list(zip("abc", list1, list2)))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# LIFO: Stacks

# browsing_session = []
# # this adds 1 into the list, the 1st thing in the stack
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)

# print(browsing_session)  # there are 3 items added to the list, to remove

# # this will remove the last item added to the list and leave 2 items in the list
# removed = browsing_session.pop()
# print(browsing_session)
# print(removed)  # last item is removed
# if not browsing_session:
#     print("disabled")
# print("redirect", browsing_session[-1])

# a falsey value can be used to see if the stack is empty

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==

# deque - allows you to take things off a list FIO but stops items in that lift having to have memory address shift

""" # collections is a module and deque is one of its classes, an object (colection of classes (?)) idea is to wrap any lists with this class so things can be taken FIFO efficiently
from collections import deque
# deque as many similar functions/ methods to list
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
if not queue:
    print("empty") """


# Tuples read only list cannot be modified, tuple is usually identified by ()

# point = (1, 2)  # this is a tuple
# however the () can be removed and python will still see this as a tuple.
# point = 1, 2
# point = 1  # would be seen as defining an integer, so a comma after defines the statement as a tuple
# point = 1,
# point = () # empty tuple
# point = (1, 2) + (3, 4)  # like a list tuple can be concatinated
# point = (1, 2) * 3  # like a list tuple can be multipled
#
# point = tuple([1, 2])  #can call the tuple function which can hold a list of iterable objects
""" point = tuple("Hello world")  # givig a list of iterable strings

point = (1, 2, 3)  #
print(point[0:2])  # like a list tuple can be iterated over
x, y, z = point  # tuple can be unpacked but canont be added to.

# if yout ry to mutate a tuple IDE usual give warning and runing will produe error
# point[0] = 10

# print(type(point)) # helps prevents modification of a list og objects
print(point) """

""" # swapping variables
x = 10
y = 11

# to swap variables you could use a third variable and set
z = x
x = y
y = z

print("x", x)
print("y", y)
# to do this on 1 line can make use of a Tuple. Tuple is defined and then unpacked

# this is the same as x, y = (11, 10) an unpacked Tuple same as a, b = 1,2
x, y = y, x
print("x", x)
print("y", y) """


""" #Arrays - these run faster than lists and usually are used for large data sets they improve performance and are imported from array module

from array import array # a module called array that contains a class called array

# the first paramater in an a array determins the type or objects to be stored, this link tells you what code to you for which type: https://docs.python.org/3/library/array.html
numbers = array("i", [1, 2, 3])
numbe.append (4) # like lists this hosts a number of methods to be used.  Note all content of the array are of the same type.  If you attempt to put in something other than the type i then the ide and system witll give an error """


# Sets this removed any duplicates from a collection. however they are unorderd collection of uniques items, and cannot be indexed like a list
# numbers = [1, 2, 3, 4, 1]
# uniques = set(numbers)  # strip out duplications
"""second = {1, 4}
second.add(5)
second.remove(5)
len(second)"""
""" print(uniques)  # resultes in no duplicates

first = set(numbers)
second = {1, 5}  # braces indicate a set

# a union of the sets but only the unique values in that union
print(first | second)

# intesection of both sets i.e. where there is commonality between both first and second
print(first & second)

# difference between the 2 sets
print(first - second)

# symetric difference number either in the 1st or 2nd set but not both (venn diagram)
print(first ^ second)

# not possible to index an array, the items are not in sequence
# print(first[0])


# to get an item from an array the exisitance for it in an array can be checked
if 1 in first:
    print("yes")
 """

""" #
# Dictionaries
# to set a dictionary { are used} string for key note for the key immutable types must be used but the value for that key can be anything
point = {"x": 1, "y": 2}
# can also use the dict function which makes use of key word arguments this is the same as above
point = dict(x=1, y=2)
# index is name of the key as dictionalirs are collections of key value pairs
point["x"] = 10
point["z"] = 20

# print(point)
# if you try and look for something that is not in the dictionary a msg is returned
if "a" in point:
    print(point["a"])
# can set what can be returned if the key is not available in this case 0
print(point.get("a", 0))
del point["x"]  # removes x from the dictionary
print(point)

# how to iterate over a dictionary
for key in point:
    print(key, point[key]) """

# ++++++++++++++++++++++++++++++++++++++
# These comprehensions can also be used with Lists [], Sets{} and Dictionaries {:}
# List
# values =[]
# for x in range(5):
#     values.append(x * 2)

# the above can reviewd to show better list comprehension
# syntax to restruct the above is [expression for item in items] we iterate over an iterable
# where range is the iterable - items, x is the item in that range function acts on, x*2 is the expression that is to be used to calcualte the result that goes into the Value list
# values = [x * 2 for x in range(5)]
# values = [x *2 for x in range(5)] # is the same as the 3 lines above

# set
# turn values = [x *2 for x in range(5)] into a set with {}
""" values = {x * 2 for x in range(5)}  # set of even values
print(values)

# Dictionaries
# this puts the results of the even numbers into key value pairs of x
values = {x: x * 2 for x in range(5)}
print(values)

# where this pattern is seen:
values = {}
for x in range(5):
    values.append(x * 2) """

# the comprehension can be used, this does not work with tuples as a generator object is returned
"""
from sys import getsizeof
values = (x * 2 for x in range(5))
print(values)
# +++++++++++++++++++++++++++++++++++++=============
# Generator expression
# as it is not efficient to store a list of values in memory esp. if that list is big or the list os a constant stream.
# this generator object produced a different memory location each time it is invoked, the object can be iterated over with the "for i in j"
values = (x * 2 for x in range(1000))
# this loop through the generator object pulling out the values printing them to screen
# give the size of the memory used for this tuple - 120, for a list
print("Generator: ", getsizeof(values))

values = [x * 2 for x in range(1000)]
# give the size of the memory used for this tuple - 120, for a list
print("list: ", getsizeof(values)) """

# Unpacking operator, can be used to take out any value from an iterable  eg when a list content is printed it is within the []
# the unpack operator takes the value out of the list
"""
numbers = [1, 2, 3]
print(numbers)
print(*numbers)
# can also take out entries of a dictionary, can upack a string as this can be iterated over

values = list(range(5))
values = [*range(5), *"hello"]
print(values)

# two list can be concatinated

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"hello"]
print(values)

# dictionary
first = {"x": 1}
second = {"x": 10, "y": 2}
# in display x in second is dsplayed not first as the key is identical
combined = {**first, **second, "z": 1}
# the last key before printing is displayed.
print(combined) """


# exercise: find the most common repeated character in the senstance = "This ia a common interview question"
""" # storing the sentance in a dictionary as the key and its frequency as the value
from pprint import pprint
sentance = "This is a common interview question"

char_frequency = {}  # empty dictionary
# for each character in the sentance:
for char in sentance:
    if char in char_frequency:  # for the key character in the dictionary if seen, increment the value by 1
        char_frequency[char] += 1
    else:
        # if the key char has not been seen before set its vlaue to 1
        char_frequency[char] = 1
# pprint is a package that will print/ format items to screen in a cleaner fashion
# pprint(char_frequency, width=1)

# now need to take the dictionary content (as these are unorderd sets), sort it and then present: take out each key value pair covert it to a tuple and then push to a list
# the list of tuples canbe easily sorted.  the sorted function takes an iterable and sorts it

 print(sorted(char_frequency.items(),
                 key=lambda kv: kv[1],
                 reverse=True))  # result here shows ascending character order
# instead of printing result for total sort of char_frquency we only need to see the first item in the now sorted list of tuples.  above becomes
char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv: kv[1],
                               reverse=True)
# this reverse sorted list now has the most frequently seen character at the start in position 0
print(char_frequency_sorted[0])

numbers = [1, 2]
print(numbers[3])

"""
"""
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("you didnt ener a valid age")
    print(ex)
    print(type(ex))
else:
    print("no exceptions were thrown")
print("execetipn continues.") """


# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("you didnt enter a valid age")
# else:
#     print("no exceptions were thrown")
# finally:
#     file.close() # this releses the open resources

# can remove the finally clause
try:
    with open("app.py") as file:  # file object thta the object retruns.
        # Files open using the with statement will autamationcally close the resource
        print("file opened.")
        # file.__enter__ and exit = context management protocol
        age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("you didnt enter a valid age")
else:
    print("no exceptions were thrown")
