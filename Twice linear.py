# question link https://www.codewars.com/kata/5672682212c8ecf83e000050
def dbl_linear(n):
    u=[1]
    for i in range (0,5*n):
        u.append(2*u[i]+1) 
        u.append(3*u[i]+1)
    u=list(set(u))
    u.sort()
    return u[n]
