# https://www.codewars.com/kata/54d496788776e49e6b00052f/python
def prim(n):
    i=1
    l=[]
    while(i<=n):
        k=0
        if(n%i==0):
            j=1
            while(j<=i):
                if(i%j==0):
                    k=k+1
                j=j+1
            if(k==2):
                l.append(i)
        i=i+1
    return l
def sum_for_list(lst):
    fa=set()
    ans=[]
    qwe=[]
    for i in lst:
        qwe=prim(abs(i))
        for j in qwe:
            fa.add(j)
    for i in fa:
        l=[]
        for j in lst:
            if j%i==0:
                l.append(j)
        ans.append([i,sum(l)])
    return sorted(ans)
