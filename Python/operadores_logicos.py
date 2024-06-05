a = True
b = False

# AND
"""
A | B | A and B
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1
"""
print(a and b)


# OR
"""
A | B | A or B
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 1
"""
print(a or b)

# NOT
"""
A | not A
0 | 1
1 | 0
"""

print(not a)