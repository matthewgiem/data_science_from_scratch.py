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
