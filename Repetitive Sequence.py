#THIS SOLUTION TIMES OUT
#https://www.codewars.com/kata/5f134651bc9687000f8022c4/train/python
def find(n):
    l=[0,1,2,2,3,3]
    if n<3:
        return l[n]
    i=6
    k=4
    j=3
    while i<=n:
        for coun in range(j): 
            l.append(k)
            if i==n:
                return l[n]
            i+=1
        k+=1
        for coun in range(j): 
            l.append(k)
            if i==n:
                return l[n]
            i+=1
        k+=1
        j+=1
    return l[n]
