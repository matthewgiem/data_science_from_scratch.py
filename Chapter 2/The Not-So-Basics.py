# Sorting

x = [4, 1, 2, 3]
y = sorted(x)           # is now [1, 2, 3, 4], x is unchanged
x.sort()                # now x is [1, 2, 3, 4]

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)           # is [-4, 3, -2, 1]
