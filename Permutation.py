# https://www.codewars.com/kata/5254ca2719453dcc0b00027d
from itertools import permutations as p
def permutations(s):
    l=set()
    se=p(s)
    for i in se:
        l.add(''.join(i))
    return list(l)
