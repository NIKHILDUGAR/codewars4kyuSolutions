def duplicate_count(text):
    text=text.lower()
    c=0
    dic=dict()
    for i in text:
        if i not in dic.keys():
            dic[i]=0
        dic[i]+=1    
        if dic[i]==2:
            c+=1
    return c
