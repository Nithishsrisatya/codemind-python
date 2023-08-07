def reverse(n):
    c=0
    while n>0:
        x=n%10
        c=c*10+x
        n=n//10
    return c
n=int(input())
s=pow(n,2)
a=reverse(n)
b=pow(a,2)
c=reverse(b)
if s==c:
    print("True")
else:
    print("False")
