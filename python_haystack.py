# Python implementation of a Haystack Data Structure.
# If that name is taken, which it probably is, idk.
# Call it what you want.
# It's not FIFO/LILO or FILO/LIFO. It's YOLO.
# This is a joke, and if nothing makes sense: good.

# because chaos
from random import randrange, randint

haystack = [] # this is where the fun starts

# there is, by design, no seek function.
# do not seek, for you shall not receive.

# is there hay in the haystack?
def isEmpty(oblivion):
    return not bool(len(oblivion))

# yeet things into thy haystack:
def throw(item, oblivion):
    oblivion.insert(randint(0, len(oblivion)), item)

# unyeet something from thy haystack:
def conjure(oblivion):
    if isEmpty(oblivion): return None
    return oblivion.pop(randrange(0, len(oblivion)))

# small example, smaller haystack:
for i in range(1, 11): throw(i, haystack)
print(haystack)
print([conjure(haystack) for _ in range(10)])

# made by a student mad at his school
# for making no sense. viva la bosti.
