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
