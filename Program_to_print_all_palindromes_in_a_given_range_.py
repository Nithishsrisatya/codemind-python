def palin(n):
    s=n
    c=0
    while n>0:
        x=n%10
        c=c*10+x
        n=n//10
    if c==s:
        return c
    else:
        return -1
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    s=palin(i)
    if s!=-1:
        l.append(s)
print(*l)