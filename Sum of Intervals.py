# https://www.codewars.com/kata/52b7ed099cdc285c300001cd
def sum_of_intervals(inl):
    set1=set()
    for (i,j) in inl:
        k=i
        while k<j:
            set1.add(k)
            k=k+1
    return (len(set1))
