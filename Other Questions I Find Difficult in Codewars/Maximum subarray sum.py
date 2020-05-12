#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/solutions/python
#BETTER Prefix sum solution 
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
    
#my initial soln
def maxSequence(arr):
    arr1=[]
    sum=0
    sum1=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum1=0
            for l in range(i,j+1):
                sum1 = sum1 + arr[l];    
            if sum1>sum:
                sum=sum1
    return sum
