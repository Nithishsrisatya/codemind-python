n=int(input())
a=0
b=1
c=0
if n==1:
    print(a)
else:
    while c<n:
        print(a,end=' ')
        d=a+b
        a=b
        b=d
        c+=1