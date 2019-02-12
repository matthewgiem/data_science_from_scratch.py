# Whitespace Formatting
for i in [1, 2, 3, 4, 5]:
    print(i)            # first line in ' for i' block
    for j in [1, 2, 3, 4, 5]:
        print(j)        # first line in 'for j' block
        print(i + j)    # last line in 'for j' block
    print(i)            # last line in 'for i' block
print('done looping')


long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11
                            12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

# incorrect way
lists_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# correct way
easier_to_read_lists_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

# \ to indicate statement continues onto the next line
two_plus_three = 2 + \
                3
import re
 my_regex = re.compile("[0-9]+", re.I)

def double(x):
    '''this is were you put an optional docstring
    that explains what the function does.
    for example, this function multiplies its input by 2'''
    return x * 2

def apply_to_one(f):
    '''calls the function f with 1 as its argument'''
    return f(1)

my_double = double              # refers to the previously defined function
x = apply_to_one(my_double)     # equals 2

y = apply_to_one(lambda x: x + 4)   # equals 5

another_double = lambda x: 2 * x    # don't do this
def another_double(x): return 2 * x # do this instesd

def my_print(message='my default message'):
    print(message)

my_print('hello')       # prints 'hello'
my_print()              # prints 'my default message'

def subtract(a=0, b=0):
    return a - b

subtract(10, 5)     # returns 5
subtract(0, 5)      # returns -5
subtract(b=5)       # returns -5

single_quoted_string = 'data science'
double_qouted_string = "data science"

tab_string = "\t"   # represents the characters
len(tab_string)     # is 1

not_tab_string = r"\t"  # represents the characters '\' and 't'
len(not_tab_string)     # is 2

multi_line_string = '''This is the first line
and this is the second line
and this is the third line'''

try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)     # equals 3
list_sum = sum(integer_list)        # equals 6

x = list(range(10)) # is the list [0, 1, 2, ..., 9] *list() needed for python 3+
zero = x[0]         # equals 0 lists are indexed at 0
one = x[1]          # equals 1
nine = x[-1]        # equals 9 'pythonic' for last element
eight = x[-2]       # equals 8 'pythonic' for next-to-last element
x[0] = -1           # now x is [-1, 1, 2,..., 9]

# slice

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:4]
last_three = x[-3:]
with_out_first_and_last = x[1:-1]
copy_of_x = [:]

1 in [1, 2, 3]  # True
0 in [1, 2, 3]  # False

x = [1, 2, 3]
x.extend([4, 5, 6])     # x is now [1, 2, 3, 4, 5, 6]

x = [1, 2, 3]
y = x + [4, 5, 6]       # y is now [1, 2, 3, 4, 5, 6]

x = [1, 2, 3]
x.append(0)             # x is now [1, 2, 3, 0]

y = x[-1]               # equals 0
z = len(x)              # equals 4

x, y = [1, 2]           # now x is 1 and y is 2

_, y = [1, 2]           # now y ==2, didn't care about the first element

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3          # muylist is now [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print('cannot modify a tuple')

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)      # equals (5, 6)
s, p = sum_and_product(2, 3)    # s equals 5 and p equals 6

x, y = 1, 2
x, y = y, x         # Pythonic way to swap veriable

# dictionaries

empty_dict = {}                     # Pythonic
empty_dict2 = dict()                # less Pythoinic
grades = {'Joel': 80, 'Tim': 95}    # dictionary literal

joels_grade = grades['Joel']        # equals 80

try:
    kates_grade = grades['Kate']
except KeyError:
    print('no grade for Kate!')

joel_has_grade = 'Joel' in grades   # True
kate_has_grade = 'Kate' in grades   # False

joels_grade = grades.get('Joel', 0)     # equals 80
kates_grade = grades.get('Kate', 0)     # equals 0
no_ones_grade = grades.get('No One')    # defalut is None

grades['Tim'] = 99                      # replaces the old value
grades['Kate'] = 100                    # creates a third entry
num_students = len(grades)              # equals 3

tweet = {
    'user': 'Joelgrus',
    'text': 'Data Science is Awesome',
    'retweet_count': 100,
    'hashtages': ['#Data', '#Science', '#datascience', '#awesome', '#yolo']
}

tweet_keys = tweet.keys()       # list of keys
tweet_values = tweet.values()   # list of values
tweet_items = tweet.items()     # list of key, value tuples

'user' in tweet_keys            # True but uses a slow list in
'user' in tweet                 # more Pythonic, users faster dict in
'Joelgrus' in tweet_values      # True

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

from collections import defaultdict
word_counts = defaultdict(int)      # int() produces 0
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)         # list() produces and empty list
dd_list[2].append(1)                # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)         # dict() produces an empty dict
dd_dict['Joel']['City'] = 'Seattle' # {'Joel': {'City': 'Seattle'}}

dd_pair defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                   # now dd_pair contains {2: [0,1]}

# Counter
from collections import Counter
c = Counter([0, 1, 2, 0])          # c is (basically {0: 2, 1: 1, 2: 1})

word_counts = Counter(document)

# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print(word, count)

# Sets

s = set()
s.add(1)    # s is now {1}
s.add(2)    # s is now {1, 2}
s.add(2)    # s is still {1, 2}
x = len(s)  # equals 2
y = 2 in s  # True
z = 3 in s  # False
