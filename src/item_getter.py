import string
from typing import Sequence

def mygetter(*args):
    # anything that can be indexed with []
    def inside_function(indexed):
        output = [ indexed[x] for x in args ]
        if len(args)==1:
            output = output[0]
        else:
            output = tuple(indexed[x] for x in args)
    
        return output
    return inside_function


g1 = mygetter(-1)
print(g1([10, 20, 30]))  # returns 30

g2 = mygetter(0, -1)
print(g2([10, 20, 30]))  # returns (10, 30)

g3 = mygetter('b')
d = {'a':1, 'b':2, 'c':3}
print(g3(d))             # returns 2