### VECTORS ###

height_weight_age = [70,    # inches,
                    170,    # pounds,
                    40]     # years

grades =            [95,    # exam 1
                    80,     # exam 2
                    75,     # exam 3
                    62]     # exam 4

# zip is used to create an itirable were a list isn't an itirable

def vector_add(v, w):
    '''adds corresponding elements'''
    return[v_i + w_i, for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    '''subtracts corresponding elements'''
    return[v_i - w_i, for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    '''take a list of vectors and sum there corresponding parts'''
    result = vectors[0]                             # start with the first vector
    for vector in vectors[1:]:                      # loop over the rest of the vectors
        result = vector_add(result, vector)         # add vectors to the result and rename result
    return result

# the same can be done by using reduce()

def reduce_vector_sum(vectors):
    return reduce(vector_add, vectors)


# or using partial()

vector_sum = partial(reduce, vector_add)            # look into how partial works

def scalar_multiply(c, v):
    '''c is a number, v is a vector'''
    return[c * v_i, for v_i in v]

def vector_mean(vectors):
    '''compute a vector whos ith element is the mean of the ith elements of the input vectors'''
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    '''v_1 * w_1 + v_2 + w_2 + ... + v_n + w_n'''
    return sum(v_i * w_i, for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    '''v_1^2 + v_2^2 + ... + v_n^2'''
    return dot(v, v)

import math

def magnitude(v):
    '''square root (v_1^2 + v_2^2 + ... + v_n^2)'''
    return math.sqrt(sum_of_squares(v))

def sqaured_distance(v, w):
    '''(v_1 - w_1)^2 + ... + (v_n - w_n)^2'''
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    '''distance = square root of ((v_1 - w_1)^2 + ... + (v_n - w_n)^2)'''
    return math.sqrt(sqaured_distance(v, w))

def cleaner_distance(v, w):
    '''cleaner way find distance using functions already created'''
    return magnitude(vector_subtract(v,w))



### MATRICES ###

# typicall use capitol letters to represent matrices

A = [[1,2,3],       # A has 2 rows and 3 columns
    [4,5,6]]

B = [[1,2],         # B has 3 rows and 2 columns
    [3,4],
    [5,6]]


#  the matrix A has len(A) rows, and len(A[0]) columns

def shape(A):
    '''returns the number of rows and columns'''
    num_rows = len(A)
    num_col = len(A[0]) if A else 0     # number of elemens in the first row
    return num_rows, num_col

def get_row(A, i):
    '''return the ith row of matrix A'''
    return A[i]                         # A[i] is already the ith row

def get_col(A, j):
    '''return the ith col of matrix A'''
    return [A_i[j]                      # jth element of row A_i
            for A_i in A]               # for each row A_i

def make_matrix(num_rows, num_cols, entry_fn):
    '''return a num_rows X num_cols matrix
    whose (i,j)th entry is entry_fn(i,j)'''
    return [[entry_fn(i, j)             # given i, create a list
            for j in range(num_cols)]   # [entry_fn(i,0), ... ]
            for i in range(num_rows)]   # create one list for each j

def is_diagonal(i, j):
    '''1's on the 'diagonal', 0's everywhere else'''
    return 1 if i == j else 0

# identity_matrix = make_matrix(5, 5, is_diagonal)
# identity_matrix = [[1, 0, 0, 0, 0],
#                     [0, 1, 0, 0, 0],
#                     [0, 0, 1, 0, 0],
#                     [0, 0, 0, 1, 0],
#                     [0, 0, 0, 0, 1]]


friendships =  [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# can be represented as a matrix
def always_zero(x,y):
    return 0
friendships_matrix = make_matrix(10, 10, always_zero)

for pair in friendships:
    friendships_matrix[pair[0]][pair[1]] = 1
    friendships_matrix[pair[1]][pair[0]] = 1

friendships_matrix =    [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]


friends_of_five = [i                                                        # only need
                    for i , is_friend in enumerate(friendships_matrix[5])   # to look at
                    if is_friend]                                           # one row
