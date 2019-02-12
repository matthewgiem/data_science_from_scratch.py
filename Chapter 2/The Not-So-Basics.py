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
