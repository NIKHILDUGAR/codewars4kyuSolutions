#https://www.codewars.com/kata/554f76dca89983cc400000bb/solutions/python
import math
def factors(n):
    fact=[]
    for i in range(1,math.floor(math.sqrt(n))+1):
        if (n%i==0):
            fact.append([int(n/i),i])
    return(fact)
def sol_equa(n):
    soln=[]
    factor=factors(n)
    for fact in factor:
        x=int(fact[0]+fact[1])/int(2)
        y=int(fact[0]-x)/int(2)
        if(math.ceil(x)==x and math.ceil(y)==y):
            soln.append([int(x),int(y)])
    return (soln)
