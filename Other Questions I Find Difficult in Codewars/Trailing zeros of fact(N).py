#https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/solutions/python

#recursive soln
def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0


#initial soln
import math
def zeros(n):
    if n<=4:
       return 0
    s=0
    k=int(math.log(n,5))
    for i in range(1,k+1):
        g=5**i
        s+=int(n/g)
    return s
