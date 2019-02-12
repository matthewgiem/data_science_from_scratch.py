# Sorting

x = [4, 1, 2, 3]
y = sorted(x)           # is now [1, 2, 3, 4], x is unchanged
x.sort()                # now x is [1, 2, 3, 4]

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)           # is [-4, 3, -2, 1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
            key=lambda (word, count): count,
            reverse=
            true)

# List Comprehensions

even_numbers = [x for x in range(5) if x % 2 == 0]          # [0, 2, 4]
squares = [x * x for x in range(5)]                         # [ 0, 1, 4, 9, 16]
even_squares = [x * x for x in range(5) if x % 2 == 0]      # [0, 4, 16]
even_squares = [x * x for x in even_numbers]

square_dict = {x : x * x for x in range(5)}                 #{0:0, 1:1, 2:4, 3:9, 4:16}
square_set = {x * x for x in [-1, 1]}                       # {1}

zeros = [0 for _ in even_numbers]                           # has the same length as even_numbers

pairs = [(x, y)
        for x in range(10)
        for y in range(10)]                                 # 100 pairs (0, 0), (0, 1)....(9, 9)

increasing pairs = [(x, y)                                  # only pairs with x < y
                    for x in range(10)                      # range(lo, hi) equals
                    for y in range(x + 1, 10)]              # [lo, lo + 1, ... , hi - 1]

# Generators and Iterators
# range(1000000) creates a actual list of 1mil items running out of memory we can use the following
# when we only want to iterate over one of the follwing at a time

def lazy_range(n):
    ''' a lazy version of range'''
    i = 0
    while i < n:
        yeild i
        i += 1

for i in lazy_range(10):
    do_something_with(i)

# this problem is fixed in python 3 and all ranges are lazy
def natural_numbers():
    '''returns 1, 2, 3, ...'''
    n = 1
    while True:
        yield n
        n += 1

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

# Randomness

import random

four_uniform_randoms = [random.random() for _ in range(4)]          # creates 4 random numbers

# not actually random
random.seed(10)
print(random.random())      # 0.5714025946899135
random.seed(10)
print(random.random())      # 0.5714025946899135

random.randrange(10)        # choose randomly from range(10) = [0, 1, 2, 3,...,8, 9]
random.rangerange(3,6)      # choose randomly from range(3, 6) = [3, 4, 5]

up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)            # shuffled list of 10 elements

my_best_friend = random.choice(['Alice', 'Bob', 'Charlie'])     # random choice from List

lottery_numbers = list(range(60))
winning_numbers = random.sample(lottery_numbers, 6)             # 6 random numbers from 60 sampling with out replacement

four_with_replacement = [random.choice(range(10))
                        for _ in range(4)]                      # 4 random numbers from 10 sampling with replacement


# Regular Expressions

import re

print(all([                                 # all of these are true, because
    not re.match("a", "cat"),               # * 'cat' doesn't start with 'a'
    re.search("a", "cat"),                  # * 'cat' has an 'a' in it
    not re.search("c", "dog"),              # * 'dog' doesn't have a 'c' init
    3 == len(re.split("[ab]", "carbs")),    # * split on a orb to ['c', 'r', 's']
    "R-D-" == re.sub("[0-9]", "-", "R2D2")  # * replace digits with dashes
]))                                         # prints True

# Object-Oriented Programming

# by convention, we give clases PascalCase names class Set:

# these are the member functions
# everyone takes a first parameter "self" (another conventiojn)
# that refers to the particular Set ofject being used

def __init__(self, values=None):
    '''This is the constructor,
    It gets called when you cr3eate a new Set
    s1 = Set()      # empty Set
    s2 = Set([1, 2, 2, 3])'''

    self.dict = {}  # each instance of Set has its own dict property
                    # which is what we'll use to track memberships
    if values is not None:
        for value in values:
            self.add(value)
def __repr__(self):
    '''this is the string representation of a Set object
    if you type it at the Python promp or pass it to str()'''
    return "Set: " + str(self.dit.keys())

# we'll represent membership by being a key in self.dict with value True
def add(self.value):
    self.dict[value] = True

# value is in the Set if it's a key in the dictionary
def contains(self, value):
    return value in self.dict

def remove(slef, value):
    del self.dict[value]

# customs class in use

s = Set([1, 2, 3])
s.add(4)
print(s.contains(4))        # True
s.remove(3)
print(s.contains(3))        # False

# Functional Tools
def exp(base, power):
    return base ** power

def two_to_the(power):
    return exp(2, power)

# better way
from functools import partial
two_to_the = partial(exp, 2)
print(two_to_the(3))        # equals 8

square_of = partial(exp, power=2)
print(square_of(3))         # equals 9

def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]      # [2, 4, 6, 8]
twice_xs = map(double, xs)              # same as above
list_doubler = partial(map, double)     # *function* that doubles a list
twice_xs = list_doubler(xs)             # again [2, 4, 6, 8]

def multiply(x, y): return x * y

products = map(mulitply, [1, 2], [4, 5])        # [1 * 4, 2 * 5] = [4, 10]

def is_even(x):
    '''True if x is even, False if x is odd'''
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]         # [2, 4]
x_evens = filter(is_even, xs)                   # same as above
list_evener = partial(filter, is_even)          # *function* that filters a list
x_evens = list_evener(xs)                       # again [2, 4]

x_product = reduce(mulitply, xs)                # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, mulitply)        # *function* that reduces a list
x_product = list_product(xs)                    # again 24

# Enumerate

# not Pythonic
for i in range(len(document)):
    document = document[i]
    do_something(i, document)

# also not Pythonic
i = 0
for document in documents:
    do_something(i, documemnt)
    i += 1

# Pythonic
for i, document in enumerate(documents):
    do_something(i, document)

# if we just want the indexes
for i in range(len(documents)): do_something(i)     # not Pythonic
for i, _ in enumerate(documents): do_something(i)   # Pythonic
