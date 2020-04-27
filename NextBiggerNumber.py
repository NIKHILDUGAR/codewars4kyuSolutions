# question link https://www.codewars.com/kata/55983863da40caa2c900004e
def next_bigger(n):
    l=list(map(int, str(n)))
    x=l[::-1]
    k=[]
    j=[]
    flag=0
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            k=x[0:i+1]
            j=x[i+1:]
            flag=1
            break
    for i in range(len(k)):
        if k[i]>j[0]:
            z=k[i]
            k[i]=j[0]
            j[0]=z
            break
    k.sort
    x=j[::-1]+k
    sum=0
    if (flag==0):
        return -1
    for i in range(len(x)):
        sum=x[i]+sum*10
    return sum
