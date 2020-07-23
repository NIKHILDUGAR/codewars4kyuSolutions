# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/python
#MY SOLUTION
def solve(s):
    
    a=sum(1 for c in s if c.isupper())
    b=sum(1 for c in s if c.islower())
    e=sum(1 for c in s if c.isnumeric())
    return [a,b,e,len(s)-(a+b+e)]

BEST SOLUTION IN MY OPINION
import re
def solve(s):
    return [len(re.findall(i,s)) for i in ('[A-Z]','[a-z]','\d','[^a-zA-Z0-9]')]

