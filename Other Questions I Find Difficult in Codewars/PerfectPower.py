#https://www.codewars.com/kata/54d4c8b08776e4ad92000835

import math
def isPP(n):
    for i in range(2,int(math.sqrt(n))+2):
        j=math.log(n,i)
        if math.ceil(round(j,5))==int(math.ceil(j)) :
            j=int(math.ceil(j)) 
            b=i**j
            if i==n:    
                return None
            if b==n:
                return [i,j]
        if math.floor(round(j,5))==int(math.floor(j)):
            j=int(math.floor(j))
            b=i**j
            if i==n:    
                return None
            if b==n:
                return [i,j]
