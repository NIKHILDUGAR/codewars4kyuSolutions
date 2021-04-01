#question link https://www.codewars.com/kata/5629db57620258aa9d000014/python

def mix(s1, s2):
    res1 = {i : s1.count(i) for i in set(s1) if i!=" " and i.islower()}
    res2 = {i : s2.count(i) for i in set(s2) if i!=" " and i.islower()}
    k=set(list(res1.keys())+list(res2.keys()))
    s=[]
    for i in k:
        c1=0
        c2=0
        try:
            if res1[i]>1:
                c1=res1[i]
        except:
            pass
        try:
            if res2[i]>1:
                c2=res2[i]
        except:
            pass
        if c1>c2:
            s.append([i,c1,1])
        if c1<c2:
            s.append([i,c2,2])
        if c1==0 and c2==0:
            continue
        elif c1==c2:
            s.append([i,c1,3])
            
    st=""
    s=sorted(s, key=lambda x: (-x[1],+x[2],ord(x[0])))
    for i in range(len(s)):
        k=s[i]
        st+= str(k[2])  +":"+str(k[0])*k[1]
        if k!=s[-1]:
            st+="/"
    st=st.replace("3:","=:")
    return st
