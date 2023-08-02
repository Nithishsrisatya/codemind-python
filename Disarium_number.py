n=int(input())
a=n
c=0
s=len(str(n))
while n>0:
    x=n%10
    c+=pow(x,s)
    n=n//10
    s-=1
if c==a:
    print("True")
else:
    print("False")