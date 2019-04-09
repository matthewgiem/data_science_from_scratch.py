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
